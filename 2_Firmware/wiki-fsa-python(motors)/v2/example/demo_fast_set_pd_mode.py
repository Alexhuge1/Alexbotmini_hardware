from fi_fsa import fi_fsa_v2
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        for i in range(len(server_ip_list)):
            fi_fsa_v2.fast_set_mode_of_operation(
                server_ip_list[i], fi_fsa_v2.FSAModeOfOperation.POSITION_CONTROL_PD
            )

        time.sleep(1)  # sleep 1 second


if __name__ == "__main__":
    main()
