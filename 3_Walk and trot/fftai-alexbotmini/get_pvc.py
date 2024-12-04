import time
import math
import torch
import numpy as np
from collections import deque
from fi_fsa import fi_fsa_v2

# define parameter
server_ip_list = ['192.168.137.101','192.168.137.10']
pos=[]
vel=[]
obs = [None] * 47
class motors:
    def init():
        server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")
        pos = [None] * len(server_ip_list)
        vel = [None] * len(server_ip_list)
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
        pos = [None] * len(server_ip_list)
        vel = [None] * len(server_ip_list)
        for i in range(len(server_ip_list)):    
            p,v,c = fi_fsa_v2.fast_get_pvc(server_ip_list[i])
            pos[i]=p
            vel[i]=v
            print(
                "Position = %f, Velocity = %f, Current = %.4f"
                % (p, v, c)
            )

if __name__ == "__main__":
    motors.init()
    motors.get_pvc()
    motors.pos_control()
    motors.get_pvc()
    motors.get_pvc()
    print(
        "Position = %f, Velocity = %f,%f,%f"
        % (pos[0], vel[0], pos[1],vel[1])
    )
