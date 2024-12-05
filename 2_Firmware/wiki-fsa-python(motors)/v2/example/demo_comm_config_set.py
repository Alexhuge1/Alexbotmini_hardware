from fi_fsa import fi_fsa_v2
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter("Actuator")

    if server_ip_list:

        # set the communication configuration of all FAS
        # Notice : set static_IP should config DHCP_enable to be False! Otherwise, it will not work!
        for i in range(len(server_ip_list)):
            dict = {
                "name": "FSA-" + str(i),
                "DHCP_enable": False,
                "SSID": "fftai-6",
                "password": "fftai2015",
                "static_IP": [192, 168, 137, i + 101],
                "gateway": [192, 168, 137, 1],
                "subnet_mask": [255, 255, 255, 0],
                "dns_1": [114, 114, 114, 114],
                "dns_2": [8, 8, 8, 8],
            }
            fi_fsa_v2.set_comm_config(server_ip_list[i], dict)

        print("\n")
        time.sleep(1)

        # get the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            fi_fsa_v2.get_comm_config(server_ip_list[i])

        print("\n")

        for i in range(len(server_ip_list)):
            fi_fsa_v2.reboot(server_ip_list[i])


if __name__ == "__main__":
    main()
