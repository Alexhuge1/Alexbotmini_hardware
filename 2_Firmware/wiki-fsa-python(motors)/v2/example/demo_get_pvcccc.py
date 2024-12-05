from fi_fsa import fi_fsa_v2
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        for i in range(10000):
            # start_time = time.time()

            for i in range(len(server_ip_list)):
                pvcccc = fi_fsa_v2.get_pvcccc(server_ip_list[i])
                print(
                    "Position = %f, Velocity = %f, Current_iq = %.4f, Current_id = %.4f, Phase_current_ib = %.4f, Phase_current_ic = %.4f"
                    % (pvcccc[0], pvcccc[1], pvcccc[2], pvcccc[3], pvcccc[4], pvcccc[5])
                )

            # end_time = time.time()
            #
            # # print the latency of the pvc function
            # latency = end_time - start_time
            # print(latency * 1000, "ms")

            time.sleep(0.2)  # sleep 1 second


if __name__ == "__main__":
    main()
