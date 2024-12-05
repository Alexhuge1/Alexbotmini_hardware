from fi_fsa import fi_fsa_v2

server_ip_list = []
filter_ip_list = []


def main():
    server_ip_list = fi_fsa_v2.broadcast_func()
    comm_root_list = []

    if server_ip_list:
        for i in range(len(server_ip_list)):
            comm_root = fi_fsa_v2.get_comm_root(server_ip_list[i])
            comm_root_list.append(comm_root)

    print("The communication root list is: ", comm_root_list)

    print("\n")

    if server_ip_list:
        for i in range(len(server_ip_list)):
            comm_root = comm_root_list[i]
            # 检测是否包含 type 字段
            if "type" in comm_root:
                # 检测 type 字段是否为 CtrlBox
                if comm_root["type"] == "CtrlBox":
                    filter_ip_list.append(server_ip_list[i])

    print("The CtrlBox ip list is: ", filter_ip_list)


if __name__ == "__main__":
    main()
