# Introduction to Control Systems

## Actuator Control Principles

### Three-Loop Servo Control

Since computer control is a type of sampled control, it can only calculate the control quantity based on the deviation at the sampling moment and cannot continuously output the control quantity like analog control for continuous control. Due to this feature, the integral and differential terms in the PID controller cannot be used directly and must be discretized. The method of discretization is as follows: let $T$ be the sampling period, and $k$ be the sampling sequence number, then the discrete sampling time $kT$ corresponds to continuous time $t$. By using numerical integration to approximate the integral with the rectangular method and using first-order backward difference to approximate the differential, the following approximations can be made:

$$
t \approx kT \quad (k = 0, 1, 2, \dots)
$$

$$
\int{e(t) dt} \approx T \sum_{j = 0}^{k} e(jT) = T \sum_{j = 0}^{k} e_{j}
$$

$$
\frac{d}{dt} e(t) \approx \frac{e(kT) - e[(k - 1) T]}{T} = \frac{e_{k} - e_{k - 1}}{T}
$$

In the above formulas, for convenience, expressions like $e(jT)$ are simplified to $e_{j}$.

#### Position Control

![FSA Control Block Diagram - Position Control](../images/FSA%E6%8E%A7%E5%88%B6%E6%A1%86%E5%9B%BE-%E4%BD%8D%E7%BD%AE%E6%8E%A7%E5%88%B6.svg)

$$
e_{j} = q_{d_{j}} - q_{j}
$$

$$
\dot{e}_ {j} = K_{p}^{pos} e_{j} G_{\theta} - \dot{q}_ {j} G_{\omega}
$$

$$
I_{q_{set_{j}}} = K_{p}^{vel} \dot{e}_ {j} + T_{\omega} K_{i}^{vel} \sum_{j = 0}^{k} \dot{e}_{j}
$$

#### Velocity Control

![FSA Control Block Diagram - Velocity Control](../images/FSA%E6%8E%A7%E5%88%B6%E6%A1%86%E5%9B%BE-%E9%80%9F%E5%BA%A6%E6%8E%A7%E5%88%B6.svg)

$$
\dot{e}_ {j} = \dot{q}_ {d_{j}} - \dot{q}_ {j} G_{\omega}
$$

$$
I_{q_{set_{j}}} = K_{p}^{vel} \dot{e}_ {j} + T_{\omega} K_{i}^{vel} \sum_{j = 0}^{k} \dot{e}_{j}
$$

#### Current Control

![FSA Control Block Diagram - Current Control](../images/FSA%E6%8E%A7%E5%88%B6%E6%A1%86%E5%9B%BE-%E7%94%B5%E6%B5%81%E6%8E%A7%E5%88%B6.svg)

Ideally, after the user specifies the $I_{q}$ value, the FSA will output a maximum torque of $\tau = K_{t} I_{q}$, where $K_{t}$ is the current-torque coefficient, determined at the factory.

> Tips:
>
> The actuator can only output a torque of $\tau = K_{t} I_{q}$ when it is in a stalled condition.

### PD Control

![FSA Control Block Diagram - PD Control](../images/FSA%E6%8E%A7%E5%88%B6%E6%A1%86%E5%9B%BE-PD%E6%8E%A7%E5%88%B6.svg)

$$
e_{j} = q_{d_{j}} - q_{j}
$$

$$
\dot{e}_ {j} = 0 - \dot{q_{j}}
$$

$$
\tau_{j} = K_{p}^{pd} e_{j} + K_{d}^{pd} \dot{e}_{j}
$$

## Symbol Table

|    Symbol     |                  Value                  |       Unit       |                      Definition                       |
| :-----------: | :-------------------------------------: | :--------------: | :---------------------------------------------------: |
|    $q_{d}$    |      Variable (determined by user)      |    $\rm{deg}$    |                    Target position                    |
|      $q$      |                Variable                 |    $\rm{deg}$    |                    Actual position                    |
|      $e$      |                Variable                 |    $\rm{deg}$    |                    Position error                     |
| $\dot{q_{d}}$ |      Variable (determined by user)      |   $\rm{deg/s}$   |                    Target velocity                    |
|   $\dot{q}$   |                Variable                 |   $\rm{deg/s}$   |                    Actual velocity                    |
|   $\dot{e}$   |                Variable                 |   $\rm{deg/s}$   |                    Velocity error                     |
| $I_{q_{set}}$ |                Variable                 |     $\rm{A}$     |                Target $Q$ axis current                |
|    $I_{q}$    |                Variable                 |     $\rm{A}$     |                Actual $Q$ axis current                |
|    $\tau$     |                Variable                 | $\rm{N \cdot m}$ |                     Target torque                     |
| $T_{\omega}$  |                  $0.2$                  |    $\rm{ms}$     |             Velocity loop control period              |
|    $K_{t}$    | Constant (determined by actuator model) |        -         |           Current-torque conversion factor            |
|      $i$      | Constant (determined by actuator model) |        -         |                    Reduction ratio                    |
|   $N_{pp}$    | Constant (determined by actuator model) |        -         |                 Number of pole pairs                  |
| $G_{\theta}$  |                   $i$                   |        -         |              Position conversion factor               |
| $G_{\omega}$  |      $\frac{i \cdot N_{pp}}{360}$       |        -         |              Velocity conversion factor               |
|   $G_{pd}$    |                $0.01745$                |        -         | $\rm{deg/s} \rightarrow \rm{rad/s}$ conversion factor |
