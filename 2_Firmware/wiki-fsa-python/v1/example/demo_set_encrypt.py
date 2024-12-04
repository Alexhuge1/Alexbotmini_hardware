from fi_fsa import fi_fsa_v1

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v1.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        # auto run one turn to set the encoder of all FAS
        for i in range(len(server_ip_list)):
            dict = {
                "username": "test",
                "password": "test",
            }
            fi_fsa_v1.encrypt(server_ip_list[i], dict)

        for i in range(len(server_ip_list)):
            fi_fsa_v1.reboot(server_ip_list[i])


if __name__ == "__main__":
    main()
