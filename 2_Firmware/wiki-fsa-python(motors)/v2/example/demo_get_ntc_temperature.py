from fi_fsa import fi_fsa_v2
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        for i in range(len(server_ip_list)):
            temperature = fi_fsa_v2.get_ntc_temperature(server_ip_list[i])
            print(
                "mos_temperature = %f, armature_temperature = %f"
                % (temperature[0], temperature[1])
            )

        # end_time = time.time()
        #
        # # print the latency of the pvc function
        # latency = end_time - start_time
        # print(latency * 1000, "ms")

        time.sleep(0.2)  # sleep 1 second


if __name__ == "__main__":
    main()
