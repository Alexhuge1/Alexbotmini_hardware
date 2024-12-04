# 在linux系统下实现控制解包PS5手柄
1.工作原理：理论上，对于所有的蓝牙/usb/2.4g手柄有用，本质上实现了对于js0的解包，而所有手柄连接的包都缓存在js0（js1/js2）
手柄在linux中叫joystick 首先插上手柄/蓝牙连接
cd /dev/input
ls
以js0,js1等文件就是手柄的输入
cat /dev/input/js0 | hexdump查看

2.代码逻辑：
初始化轴名称字典 axis_names
初始化按钮名称字典 button_names
初始化轴映射列表 axis_map
初始化按钮映射列表 button_map

定义函数 ps5_open(device_path):
    尝试打开设备文件 device_path 用于读取
    打印打开设备的提示信息

定义主程序流程:
    调用 ps5_open 函数以打开 PS5 手柄设备
    获取并打印设备名称
    获取并打印轴的数量和名称
    获取并打印按钮的数量和名称

进入主事件循环:
    循环开始
        从设备读取事件缓冲区数据
        如果读取到数据:
            解析数据以获取时间戳、值、类型和编号

            如果是按钮事件:
                根据编号查找按钮名称
                如果按钮被按下，打印按钮名称和 "pressed"
                如果按钮被释放，打印按钮名称和 "released"

            如果是轴事件:
                根据编号查找轴名称
                对于特定的轴，取反其值
                如果轴值超过或低于特定阈值:
                    将轴值标准化为0到1之间的值
                    打印轴名称和标准化后的值

        循环结束条件为 False（即无限循环)

结束程序

REF：https://blog.csdn.net/rzdyzx/article/details/101483596