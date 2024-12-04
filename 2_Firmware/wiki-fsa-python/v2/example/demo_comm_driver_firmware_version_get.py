from fi_fsa import fi_fsa_v2
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter("Actuator")

    if server_ip_list:

        # get the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            driver_version = fi_fsa_v2.get_comm_driver_version(server_ip_list[i])
            
            firmware_version = fi_fsa_v2.get_comm_firmware_version(server_ip_list[i])

            print("{{\"driver_version\":\"{}\"}}".format(driver_version))

            print("{{\"firmware_version\":\"{}\"}}".format(firmware_version)
)
        time.sleep(1)


if __name__ == "__main__":
    main()
