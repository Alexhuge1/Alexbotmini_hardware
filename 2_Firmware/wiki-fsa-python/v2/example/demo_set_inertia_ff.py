from fi_fsa import fi_fsa_v2
import time

# server_ip_list = ["192.168.137.101"]


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        for i in range(len(server_ip_list)):
            inertia_ff = 0.5
            ret = fi_fsa_v2.set_inertia_ff(server_ip_list[i], inertia_ff)
            print(ret)

        time.sleep(1)  # sleep 1 second


if __name__ == "__main__":
    main()
