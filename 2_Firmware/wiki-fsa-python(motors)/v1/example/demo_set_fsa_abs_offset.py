from fi_fsa import fi_fsa_v1
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v1.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        for i in range(len(server_ip_list)):
            offset = 179.868164
            ret = fi_fsa_v1.set_fsa_abs_offset(server_ip_list[i], offset)
            print(ret)

        # end_time = time.time()
        #
        # # print the latency of the pvc function
        # latency = end_time - start_time
        # print(latency * 1000, "ms")

        time.sleep(0.2)  # sleep 1 second


if __name__ == "__main__":
    main()
