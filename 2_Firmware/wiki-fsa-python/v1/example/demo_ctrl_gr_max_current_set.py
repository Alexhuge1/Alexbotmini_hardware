from fi_fsa import fi_fsa_v1
import time
from fi_fsa_v1 import fi_fsa_v1_predefine
import json

server_ip_list = []

max_current_dict = {
    "192.168.137.30": 3.3,
    "192.168.137.10": 3.3,
    "192.168.137.31": 3.3,
    "192.168.137.11": 3.3,
    "192.168.137.32": 2.7,
    "192.168.137.12": 2.7,
    "192.168.137.33": 2.7,
    "192.168.137.13": 2.7,
    "192.168.137.34": 2.7,
    "192.168.137.14": 2.7,
    "192.168.137.35": 2,
    "192.168.137.15": 2,
    "192.168.137.36": 2,
    "192.168.137.16": 2,
    "192.168.137.37": 2,
    "192.168.137.17": 2,
    "192.168.137.90": 20,
    "192.168.137.91": 20,
    "192.168.137.92": 20,
    "192.168.137.93": 2,
    "192.168.137.94": 2,
    "192.168.137.95": 2,
    "192.168.137.50": 15,
    "192.168.137.70": 15,
    "192.168.137.51": 20,
    "192.168.137.71": 20,
    "192.168.137.52": 80,
    "192.168.137.72": 80,
    "192.168.137.53": 80,
    "192.168.137.73": 80,
    "192.168.137.74": 3.3,
    "192.168.137.54": 3.3,
    "192.168.137.75": 3.3,
    "192.168.137.55": 3.3,
}


def main():
    server_ip_list = fi_fsa_v1.broadcast_func_with_filter(filter_type="Actuator")

    if server_ip_list:

        # get the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            data = fi_fsa_v1.get_config_data(server_ip_list[i])

            time.sleep(1)
            json_obj = json.loads(data.decode("utf-8"))
            json_obj["motor_max_current"] = max_current_dict[server_ip_list[i]]
            if "actuator_comm_hardware_type" not in json_obj:
                json_obj["actuator_comm_hardware_type"] = 0
            fi_fsa_v1.set_config(server_ip_list[i], json_obj)

        time.sleep(1)
        for i in range(len(server_ip_list)):
            fi_fsa_v1.get_config(server_ip_list[i])

        print("\n")

        # reboot all FSA
        for i in range(len(server_ip_list)):
            fi_fsa_v1.reboot(server_ip_list[i])
        print("\n")
        time.sleep(1)


if __name__ == "__main__":
    main()
