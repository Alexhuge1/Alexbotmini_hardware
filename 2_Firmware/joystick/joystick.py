import os, struct, array
from fcntl import ioctl

print('Welcome to alexbot joystick')

axis_names = {
    0x00: 'abs_lx',  # 左摇杆X轴
    0x01: 'abs_ly',  # 左摇杆Y轴
    0x02: 'abs_rx',  # 右摇杆X轴
    0x05: 'abs_ry',  # 右摇杆Y轴
    0x03: 'abs_l2',  # R2触发器
    0x04: 'abs_r2',  # L2触发器
    0x10: 'corss_x', # 十字X轴
    0x11: 'cross_y', # 十字Y轴
   }

button_names = {
    0x130: 'button_square',   # 正方形键（□按钮）
    0x131: 'button_cross',    # 交叉键（X按钮）
    0x132: 'button_circle',   # 圆形键（O按钮）
    0x133: 'button_triangle', # 三角形键（Δ按钮）
    0x134: 'button_l1',       # L1按钮
    0x135: 'button_r1',       # R1按钮
    0x136: 'button_l2',       # l2按钮
    0x137: 'button_r2',       # r2按钮   
    0x138: 'button_options',  # Options按钮
    0x139: 'button_create',   # Create按钮
    0x13c: 'button_ps',       # PS按钮
    0x13d: 'button_pad',      # Pad按钮  
   }

axis_map = []
button_map = []

# 打开PS5手柄设备
fn = '/dev/input/js0'
print('Opening %s...' % fn)
jsdev = open(fn, 'rb')
def ps5_open(device_path='/dev/input/js0'):
    fn = '/dev/input/js0'
    print('Opening %s...' % fn)
    jsdev = open(fn, 'rb')

# Get the device name.
#buf = bytearray(63)
buf = array.array('B', [0] * 64)
ioctl(jsdev, 0x80006a13 + (0x10000 * len(buf)), buf) # JSIOCGNAME(len)
js_name = buf.tobytes().rstrip(b'\x00').decode('utf-8')
print('Device name: %s' % js_name)
 
# Get number of axes and buttons.
buf = array.array('B', [0])
ioctl(jsdev, 0x80016a11, buf) # JSIOCGAXES
num_axes = buf[0]
 
buf = array.array('B', [0])
ioctl(jsdev, 0x80016a12, buf) # JSIOCGBUTTONS
num_buttons = buf[0]
 
# Get the axis map.
buf = array.array('B', [0] * 0x40)
ioctl(jsdev, 0x80406a32, buf) # JSIOCGAXMAP
 
for axis in buf[:num_axes]:
    axis_name = axis_names.get(axis, 'unknown(0x%02x)' % axis)
    axis_map.append(axis_name)
 
# Get the button map.
buf = array.array('H', [0] * 200)
ioctl(jsdev, 0x80406a34, buf) # JSIOCGBTNMAP
 
for btn in buf[:num_buttons]:
    btn_name = button_names.get(btn, 'unknown(0x%03x)' % btn)
    button_map.append(btn_name)
 
print('%d axes found: %s' % (num_axes, ', '.join(axis_map)))
print('%d buttons found: %s' % (num_buttons, ', '.join(button_map)))

# Main event loop
while True:
    evbuf = jsdev.read(8)
    if evbuf:
        time, value, type, number = struct.unpack('IhBB', evbuf) #图中标出的数字是指此处的 number，用来判断此词数据是哪个按键的变化
        if type & 0x01:
            button = button_map[number]
            if button:
                button_names[button] = value
                if value:
                    print("%s pressed" % (button))
                else:
                    print("%s released" % (button))
 
        if type & 0x02:
            axis = axis_map[number]
            if number==0x01 :
                value=-value
            if number==0x05 :
                value=-value
            
            if value > 5000:
                fvalue = value / 32767.0
                axis_names[axis] = fvalue
                print("%s: %.3f" % (axis, fvalue))
            if value < -5000:
                fvalue = value / 32767.0
                axis_names[axis] = fvalue
                print("%s: %.3f" % (axis, fvalue))