import time
import math
import torch
import numpy as np
from collections import deque
from fi_fsa import fi_fsa_v2

class robot:
    # define parameter
    server_ip_list = ['192.168.137.101','192.168.137.10',]
    pos = []   # 12D
    vel = []   # 12D
    obs = [] # 47D

    class cmd:
        vx = 0.4
        vy = 0.0
        dyaw = 0.0

    class robot_config:
                kps = np.array([200, 200, 350, 350, 15, 15, 200, 200, 350, 350, 15, 15], dtype=np.double)
                kds = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], dtype=np.double)
                tau_limit = 200. * np.ones(12, dtype=np.double)

    class env:
            # change the observation dim
            frame_stack = 15
            c_frame_stack = 3
            num_single_obs = 47
            num_observations = int(frame_stack * num_single_obs)
            single_num_privileged_obs = 73
            num_privileged_obs = int(c_frame_stack * single_num_privileged_obs)
            num_actions = 12
            num_envs = 4096
            episode_length_s = 24     # episode length in seconds
            use_ref_actions = False   # speed up training by using reference actions

    class normalization:
            class obs_scales:
                lin_vel = 2.0
                ang_vel = 0.25
                dof_pos = 1.0
                dof_vel = 0.05
                quat = [0, 0, 0, 1]
                height_measurements = 5.0
            clip_observations = 100.
            clip_actions = 100.
            dt = 0.001
            # action scale: target angle = actionScale * action + defaultAngle
            action_scale = 0.25
            # decimation: Number of control action updates @ sim DT per policy DT
            decimation = 10  # 100hz

    class motors:
        def init():
            server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")
            if server_ip_list:
                # enable all the motors
                for i in range(len(server_ip_list)):
                    fi_fsa_v2.set_enable(server_ip_list[i])

                # set work at position control mode
                for i in range(len(server_ip_list)):
                    fi_fsa_v2.set_mode_of_operation(
                        server_ip_list[i], fi_fsa_v2.FSAModeOfOperation.POSITION_CONTROL
                    )

                # set position control to 0.0
                for i in range(len(server_ip_list)):
                    fi_fsa_v2.set_position_control(server_ip_list[i], 0.0)
                time.sleep(8)

        def pos_control():
            global pos, vel, server_ip_list
            set_position = 180  # [deg]
            for i in range(len(server_ip_list)):
                fi_fsa_v2.fast_set_position_control(server_ip_list[i], set_position)

        def get_pvc():
            global pos, vel, server_ip_list
            # server_ip_list 已经包含了所有电机的IP地址
            # 初始化 pos 和 vel 为包含零的 NumPy 数组，长度与 server_ip_list 相同
            pos = np.zeros(len(server_ip_list), dtype=np.double)
            vel = np.zeros(len(server_ip_list), dtype=np.double)

            for i in range(len(server_ip_list)):
                p, v, c = fi_fsa_v2.fast_get_pvc(server_ip_list[i])
                # 直接将获取的值赋给对应的 NumPy 数组元素
                pos[i] = p
                vel[i] = v
                print("Position = %f, Velocity = %f, Current = %.4f" % (p, v, c))
            pos = np.array(pos, dtype=np.double)
            vel = np.array(vel, dtype=np.double)
            # 返回更新后的 pos 和 vel
            return pos, vel

class utils:
    def quaternion_to_euler_array(quat):
        # Ensure quaternion is in the correct format [x, y, z, w]
        x, y, z, w = quat

        # Roll (x-axis rotation)
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = np.arctan2(t0, t1)

        # Pitch (y-axis rotation)
        t2 = +2.0 * (w * y - z * x)
        t2 = np.clip(t2, -1.0, 1.0)
        pitch_y = np.arcsin(t2)

        # Yaw (z-axis rotation)
        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = np.arctan2(t3, t4)

        # Returns roll, pitch, yaw in a NumPy array in radians
        return np.array([roll_x, pitch_y, yaw_z])

    def pd_control(target_q, q, kp, target_dq, dq, kd):
        #Calculates torques from position commands
        return (target_q - q) * kp + (target_dq - dq) * kd

    def run(policy):
        global pos, vel, server_ip_list
        target_q = np.zeros((robot.env.num_actions), dtype=np.double)
        action = np.zeros((robot.env.num_actions), dtype=np.double)

        hist_obs = deque()
        for _ in range(robot.env.frame_stack):
            hist_obs.append(np.zeros([1, robot.env.num_single_obs], dtype=np.double))

        count_lowlevel = 0
        global pos, vel, server_ip_list
        hist_obs = deque()
         # 1000hz -> 100hz
        if count_lowlevel % 10 == 0:
            robot.motors.get_pvc()
            # Obtain an observation
            q = np.array(pos)
            dq = np.array(vel)
            obs = np.zeros([1, robot.env.num_single_obs], dtype=np.float32)
            eu_ang = utils.quaternion_to_euler_array(robot.normalization.obs_scales.quat)
            eu_ang[eu_ang > math.pi] -= 2 * math.pi

            # Get obs
            obs[0, 0] = math.sin(2 * math.pi * count_lowlevel * robot.normalization.dt  / 0.64)
            obs[0, 1] = math.cos(2 * math.pi * count_lowlevel * robot.normalization.dt  / 0.64)
            obs[0, 2] = robot.cmd.vx * robot.normalization.obs_scales.lin_vel
            obs[0, 3] = robot.cmd.vy * robot.normalization.obs_scales.lin_vel
            obs[0, 4] = robot.cmd.dyaw * robot.normalization.obs_scales.ang_vel
            obs[0, 5:17] = q * robot.normalization.obs_scales.dof_pos
            obs[0, 17:29] = dq * robot.normalization.obs_scales.dof_vel
            obs[0, 29:41] = action
            #obs[0, 41:44] = omega
            #obs[0, 44:47] = eu_ang
            obs = np.clip(obs, robot.normalization.clip_observations, robot.normalization.clip_observations)

            # maintain the scale of obs, put the newest in queue
            hist_obs.append(obs)
            hist_obs.popleft()

            policy_input = np.zeros([1, robot.env.num_observations], dtype=np.float32)
            for i in range(robot.env.frame_stack):
                policy_input[0, i * robot.env.num_single_obs : (i + 1) * robot.env.num_single_obs] = hist_obs[i][0, :]
            action[:] = policy(torch.tensor(policy_input))[0].detach().numpy()
            action = np.clip(action, -robot.normalization.clip_actions, robot.normalization.clip_actions)
            target_q = action * robot.normalization.action_scale

        target_dq = np.zeros((robot.env.num_actions), dtype=np.double)
        count_lowlevel += 1


if __name__ == '__main__':
    load_model = '/home/nvidia/fftai-alexbotmini/loadmodel/policy_example.pt'
    policy = torch.jit.load(load_model)
    utils.run(policy)


