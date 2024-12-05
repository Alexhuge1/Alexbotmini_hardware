from fi_fsa import fi_fsa_v1
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v1.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        # set the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            dict = {
                "motor_max_speed_imm": 3000,
                "motor_max_acceleration_imm": 60000,
                "motor_max_current_imm": 8,
            }
            fi_fsa_v1.set_control_param_imm(server_ip_list[i], dict)

        print("\n")
        time.sleep(1)

        # get the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            fi_fsa_v1.get_control_param_imm(server_ip_list[i])


if __name__ == "__main__":
    main()
