# Actuator-FSA-Wiki

## 文件目录说明

```shell
.
├── README.md                    # 英文 README
├── README_CN.md                 # 中文 README
│
├── doc/                         # 文档
│   ├── chinese/                 # 中文文档
│   ├── english/                 # 英文文档
│   └── images/                  # 图片
│
├── v1/                          # Python SDK V1 库与示例脚本
│   ├── example/                 # 示例脚本
│   ├── pyscurve/                # 轨迹规划相关脚本
│   ├── fi_config.py             # 配置
│   ├── fi_fsa_predefine.py      # 预定义
│   ├── fi_fsa_v1.py             # 主要功能
│   └── fi_logger.py             # 日志
│
└── v2/                          # Python SDK V2 库与示例脚本
    ├── example/                 # 示例脚本
    ├── pyscurve/                # 轨迹规划相关脚本
    ├── fi_config.py             # 配置
    ├── fi_fsa_predefine.py      # 预定义
    ├── fi_fsa_v2.py             # 主要功能
    └── fi_logger.py             # 日志
```

## 上手指南

### 开发环境

`Python >= 3.10.12`

安装 Python SDK V1 和 V2：

```shell
pip install fi_fsa
```

### 克隆仓库

```shell
git clone https://gitee.com/FourierIntelligence/wiki-fsa.git -b python
```

### 通信配置

使用网线将计算机与 FSA 连接，并将对应的网卡设置为静态 IP `192.168.137.1`。

> 若要更新 FSA 固件，则需开启共享网络。

### 运行示例脚本

将 FSA 接通电源，进入 `v1` 或 `v2` 目录，执行想要运行的示例脚本，例如：

```shell
cd v2/example # 或 cd v1/example
python ./demo_lookup.py
```

`demo_lookup.py` 脚本将会扫描所有 `192.168.137.xxx` 网段下的所有 FSA 并打印出来。

> 若要驱动电机，则需接通 48V 直流电源，若仅与电机通信，只需接通 USB 供电。

## 开发指南

### FSA 控制原理

 [Control_System_Introduction_CN.md](doc/CN/Control_System_Introduction_CN.md) 

### API 文档

 [V1_Python_API_Introduction_CN.md](doc/CN/V1_Python_API_Introduction_CN.md) 

 [V2_Python_API_Introduction_CN.md](doc/CN/V2_Python_API_Introduction_CN.md) 
