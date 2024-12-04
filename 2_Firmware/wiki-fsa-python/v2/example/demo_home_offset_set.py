import numpy

from fi_fsa import fi_fsa_v2
import time

server_ip_list = []


def main():
    server_ip_list = fi_fsa_v2.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        home_offset = numpy.ones(len(server_ip_list)) * 10

        for i in range(len(server_ip_list)):
            fi_fsa_v2.set_home_offset(server_ip_list[i], home_offset[i])

        print("\n")

        for i in range(len(server_ip_list)):
            fi_fsa_v2.get_home_offset(server_ip_list[i])

        print("\n")

        # Notice: home offset is not saved in flash, unless you obviously save it.
        # for i in range(len(server_ip_list)):
        #     fi_fse.save_config(server_ip_list[i])
        # print('\n')

        # reboot all FAS
        for i in range(len(server_ip_list)):
            fi_fsa_v2.reboot(server_ip_list[i])


if __name__ == "__main__":
    main()
