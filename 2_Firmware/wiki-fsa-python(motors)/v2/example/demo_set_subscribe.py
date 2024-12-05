from fi_fsa import fi_fsa_v2
import time
import socket
import struct

server_ip_list = []
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", 0))
addr_not_use, port = udp_socket.getsockname()
print("Socket is bound to port:", port)


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        config = {
            "port": port,
            "enable": 1,
            "position": 1,
            "velocity": 1,
            "current": 1,
            "torque": 1,
        }

        for i in range(len(server_ip_list)):
            fi_fsa_v2.set_subscribe(server_ip_list[i], config)

        if config["enable"]:
            while True:
                data, addr = udp_socket.recvfrom(2048)
                print(": Server received from {}:{}".format(addr, data))
                print(len(data))
                # pi = position_index pv = position_value vi = velocity_index vv = velocity_value
                pi, pv, vi, vv, ci, cv, ti, tv = struct.unpack(
                    ">BfBfBfBf", data[0 : 1 + 4 + 1 + 4 + 1 + 4 + 1 + 4]
                )
                print("index = %x, value = %f" % (pi, pv))
                print("index = %x, value = %f" % (vi, vv))
                print("index = %x, value = %f" % (ci, cv))
                print("index = %x, value = %f" % (ti, tv))

        print("\n")
        time.sleep(1)


if __name__ == "__main__":
    main()
