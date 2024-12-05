# from fi_fsa import fi_fsa_v2
# import time

# server_ip_list = ["192.168.137.161","192.168.137.162","192.168.137.163","192.168.137.164"]


# def main():
#     # server_ip_list = fi_fsa_v2.broadcast_func()

#     if server_ip_list:

#         for i in range(len(server_ip_list)):
#             fi_fsa_v2.get_config(server_ip_list[i])
#         for i in range(len(server_ip_list)):
#             dict = {
#                 'actuator_type': fi_fsa_v2.FSAActuatorType.TYPE_60_120.value,  # use None to not set here, if use not None, it will be set
#                 'motor_number': 1,
#                 'reduction_ratio': 120*3,  # 40:1
#                 'encoder_resolution': 4000,  # 4000 pulse/rev
#             }
#             fi_fsa_v2.set_config(server_ip_list[i], dict)

#         for i in range(len(server_ip_list)):
#             pvc = fi_fsa_v2.get_pvc(server_ip_list[i])
#             print("Position = %.2f, Velocity = %.3f, Current = %.4f" % (pvc[0], pvc[1], pvc[2]))
#             time.sleep(0.01)
#             # fi_fsa_v2.set_home_offset_group(server_ip_list[i])

#         # control_mode = "P"

#         # if control_mode == "C":
#         #     # set current control current to 0.0
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_current_control(server_ip_list[i], 0.0)
#         #     print('set current 1\n')
#         #     time.sleep(1)

#         #     # set work at current control mode
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_mode_of_operation(server_ip_list[i], fi_fsa_v2.FSAModeOfOperation.CURRENT_CLOSE_LOOP_CONTROL.value[0])
#         #     print('set mode\n')
#         #     time.sleep(1)

#         #     # enable all the motors
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_enable(server_ip_list[i])
#         #     print('enable \n')
#         #     time.sleep(1)


#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_current_control(server_ip_list[i],-1.3)
#         #     print('set current 2\n')

#         # elif control_mode == "V":
#         #     # set current control current to 0.0
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_velocity_control(server_ip_list[i], 0.0)
#         #     print('set velocity 1\n')
#         #     time.sleep(1)

#         #     # set work at velocity control mode
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_mode_of_operation(server_ip_list[i], fi_fsa_v2.FSAModeOfOperation.VELOCITY_CONTROL.value[0])
#         #     print('set mode\n')
#         #     time.sleep(1)

#         #     # enable all the motors
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_enable(server_ip_list[i])
#         #     print('enable \n')
#         #     time.sleep(1)

#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_velocity_control(server_ip_list[i], -10)
#         #     print('set velocity 2\n')

#         # elif control_mode == "P":
#         #     # set current control current to 0.0
#         #     pvc = fi_fsa_v2.get_pvc(server_ip_list[0])
#         #     try:
#         #         print("Position = %.2f, Velocity = %.3f, Current = %.4f" % (pvc[0], pvc[1], pvc[2]))
#         #     except:
#         #         pass
#         #     time.sleep(0.01)
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_position_control(server_ip_list[i], pvc[0])
#         #     print('set position 1\n')
#         #     time.sleep(1)
#         #     # set work at current control mode
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_mode_of_operation(server_ip_list[i], fi_fsa_v2.FSAModeOfOperation.POSITION_CONTROL.value[0])
#         #     print('set mode\n')
#         #     time.sleep(1)

#         #     # enable all the motors
#         #     for i in range(len(server_ip_list)):
#         #         fi_fsa_v2.set_enable(server_ip_list[i])
#         #     print('enable \n')
#         #     time.sleep(1)


#         #     for i in range(500):
#         #         pvc = fi_fsa_v2.get_pvc(server_ip_list[0])
#         #         try:
#         #             print("Position = %.2f, Velocity = %.3f, Current = %.4f" % (pvc[0], pvc[1], pvc[2]))
#         #         except:
#         #             pass
#         #         time.sleep(0.01)
#         #         if control_mode == "P":
#         #             fi_fsa_v2.set_position_control(server_ip_list[0], -i/50)

#         #     for i in range(500):
#         #         pvc = fi_fsa_v2.get_pvc(server_ip_list[0])
#         #         try:
#         #             print("Position = %.2f, Velocity = %.3f, Current = %.4f" % (pvc[0], pvc[1], pvc[2]))
#         #         except:
#         #             pass
#         #         time.sleep(0.01)
#         #         if control_mode == "P":
#         #             fi_fsa_v2.set_position_control(server_ip_list[0], -10+i/50)
#         #     print('set position 2\n')

#         for i in range(20):
#             pvc = fi_fsa_v2.get_pvc(server_ip_list[0])
#             try:
#                 print("Position = %.2f, Velocity = %.3f, Current = %.4f" % (pvc[0], pvc[1], pvc[2]))
#             except:
#                 pass
#             time.sleep(0.01)

#         for i in range(len(server_ip_list)):
#             fi_fsa_v2.set_disable(server_ip_list[i])

#         print('disable\n')
#         time.sleep(1)


# if __name__ == '__main__':
#     main()


# from fi_fsa import fi_fsa_v2
# import time


# def main():

#     cycle_times = 20
#     control_mode = "C"
#     control_current = -1.3
#     control_velocity = -10
#     control_position_delta = 0.2

#     print("\n>>====================================================================================================<<")
#     print(">>====== Prepare!!!! ======<<\n")

#     server_ip_list = fi_fsa_v2.broadcast_func()
#     if server_ip_list:

#         fi_fsa_v2.set_mode_of_operation(server_ip_list[0], fi_fsa_v2.FSAModeOfOperation.POSITION_CONTROL)
#         fi_fsa_v2.set_position_control(server_ip_list[0], 0.0)
#         fi_fsa_v2.set_enable(server_ip_list[0])
#         time.sleep(1)
#         fi_fsa_v2.set_disable(server_ip_list[0])
#         fi_fsa_v2.set_velocity_control(server_ip_list[0], 0.0)
#         fi_fsa_v2.set_current_control(server_ip_list[0], 0.0)
#         fi_fsa_v2.get_config(server_ip_list[0])

#         print("\n>>====== Start!!!! ======<<\n")

#         for i in range(cycle_times):

#             if control_mode == "C":
#                 fi_fsa_v2.set_mode_of_operation(server_ip_list[0], fi_fsa_v2.FSAModeOfOperation.CURRENT_CLOSE_LOOP_CONTROL)
#                 fi_fsa_v2.set_current_control(server_ip_list[0], control_current)
#                 fi_fsa_v2.set_enable(server_ip_list[0])
#             elif control_mode == "V":
#                 fi_fsa_v2.set_mode_of_operation(server_ip_list[0], fi_fsa_v2.FSAModeOfOperation.VELOCITY_CONTROL)
#                 fi_fsa_v2.set_enable(server_ip_list[0])
#                 fi_fsa_v2.set_velocity_control(server_ip_list[0], control_velocity)
#             elif control_mode == "P":
#                 fi_fsa_v2.set_mode_of_operation(server_ip_list[0], fi_fsa_v2.FSAModeOfOperation.POSITION_CONTROL)
#                 fi_fsa_v2.set_enable(server_ip_list[0])

#             for i in range(5):
#                 if control_mode == "P":
#                     pvc = fi_fsa_v2.get_pvc(server_ip_list[0])
#                     if pvc:
#                         fi_fsa_v2.set_position_control(server_ip_list[0], pvc[0] + control_position_delta)
#                 time.sleep(0.2)

#             pvc = fi_fsa_v2.get_pvc(server_ip_list[0])
#             try:
#                 print("\n>>------ Position = %.2f, Velocity = %.3f, Current = %.4f ------<<\n" % (pvc[0], pvc[1], pvc[2]))
#             except:
#                 pass

#         fi_fsa_v2.set_disable(server_ip_list[0])
#         time.sleep(1)

#     print("\n>>====== Stop!!!! ======<<")
#     print(">>====================================================================================================<<\n")


# if __name__ == '__main__':
#     main()


from fi_fsa import fi_fsa_v2
import time


def main():

    cycle_times = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    control_velocity = [-5, -15, -25, -15, -5, 5, 15, 25, 15, 5]

    print(
        "\n>>====================================================================================================<<"
    )
    print(">>====== Prepare!!!! ======<<\n")

    server_ip_list = fi_fsa_v2.broadcast_func()
    if server_ip_list:

        fi_fsa_v2.set_mode_of_operation(
            server_ip_list[0], fi_fsa_v2.FSAModeOfOperation.POSITION_CONTROL
        )
        fi_fsa_v2.set_position_control(server_ip_list[0], 0.0)
        fi_fsa_v2.set_enable(server_ip_list[0])
        time.sleep(1)
        fi_fsa_v2.set_disable(server_ip_list[0])
        fi_fsa_v2.set_velocity_control(server_ip_list[0], 0.0)
        fi_fsa_v2.set_current_control(server_ip_list[0], 0.0)
        fi_fsa_v2.get_config(server_ip_list[0])

        print("\n>>====== Start!!!! ======<<\n")

        for i in range(len(cycle_times)):
            for j in range(cycle_times[i]):

                fi_fsa_v2.set_mode_of_operation(
                    server_ip_list[0], fi_fsa_v2.FSAModeOfOperation.VELOCITY_CONTROL
                )
                fi_fsa_v2.set_enable(server_ip_list[0])
                fi_fsa_v2.set_velocity_control(server_ip_list[0], control_velocity[i])
                time.sleep(1)

                pvc = fi_fsa_v2.get_pvc(server_ip_list[0])
                try:
                    print(
                        "\n>>------ Position = %.2f, Velocity = %.3f, Current = %.4f ------<<\n"
                        % (pvc[0], pvc[1], pvc[2])
                    )
                except:
                    pass

        fi_fsa_v2.set_disable(server_ip_list[0])
        time.sleep(1)

    print("\n>>====== Stop!!!! ======<<")
    print(
        ">>====================================================================================================<<\n"
    )


if __name__ == "__main__":
    main()
