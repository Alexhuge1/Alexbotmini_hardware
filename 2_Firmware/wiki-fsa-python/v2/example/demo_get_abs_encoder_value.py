from fi_fsa import fi_fsa_v2
import time

server_ip_list = ["192.168.137.104"]


def main():
    # server_ip_list = fi_fsa_v2.broadcast_func()

    if server_ip_list:

        for j in range(10000):

            for i in range(len(server_ip_list)):
                angle = fi_fsa_v2.get_abs_encoder_angle(server_ip_list[i])
                print("Angle = %f" % angle)

            time.sleep(0.2)  # sleep 1 second


if __name__ == "__main__":
    main()
