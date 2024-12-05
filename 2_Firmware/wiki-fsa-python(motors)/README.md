# Actuator-FSA-Wiki

## Directory Structure

```shell
.
├── README.md                    # English README
├── README_CN.md                 # Chinese README
│
├── doc/                         # Documentation
│   ├── chinese/                 # Chinese Documentation
│   ├── english/                 # English Documentation
│   └── images/                  # Images
│
├── v1/                          # Python SDK V1 Library and Example Scripts
│   ├── example/                 # Example Scripts
│   ├── pyscurve/                # Trajectory Planning Scripts
│   ├── fi_config.py             # Configuration
│   ├── fi_fsa_predefine.py      # Predefined Settings
│   ├── fi_fsa_v1.py             # Main Functions
│   └── fi_logger.py             # Logging
│
└── v2/                          # Python SDK V2 Library and Example Scripts
    ├── example/                 # Example Scripts
    ├── pyscurve/                # Trajectory Planning Scripts
    ├── fi_config.py             # Configuration
    ├── fi_fsa_predefine.py      # Predefined Settings
    ├── fi_fsa_v2.py             # Main Functions
    └── fi_logger.py             # Logging
```

## Getting Started

### Development Environment

`Python >= 3.10.12`

Install Python SDK V1 & V2:

```shell
pip install fi_fsa
```

### Clone the Repository

```shell
git clone https://gitee.com/FourierIntelligence/wiki-fsa.git -b python
```

### Communication Configuration

Connect the computer to the FSA using an Ethernet cable and set the corresponding network card to the static IP `192.168.137.1`.

> To update the FSA firmware, network sharing must be enabled.

### Running Example Scripts

Power on the FSA, navigate to the `v1` or `v2` directory, and execute the desired example script, for example:

```shell
cd v2/example # or cd v1/example
python ./demo_lookup.py
```

The `demo_lookup.py` script will scan all FSAs in the `192.168.137.xxx` subnet and print them.

> To drive the motor, a 48V DC power supply is required. For communication with the motor only, USB power is sufficient.

## Developer Guide

### FSA Control Principle

 [Control_System_Introduction_EN.md](doc/EN/Control_System_Introduction_EN.md) 

### API Documentation

 [V1_Python_API_Introduction_EN.md](doc/EN/V1_Python_API_Introduction_EN.md) 

 [V2_Python_API_Introduction_EN.md](doc/EN/V2_Python_API_Introduction_EN.md) 
