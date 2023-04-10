import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl
import board
import digitalio

# These correspond to the pins on the Raspberry Pi Pico
btn1_pin = board.GP1
btn2_pin = board.GP2
btn3_pin = board.GP3
btn4_pin = board.GP4
btn5_pin = board.GP5
btn6_pin = board.GP6
btn7_pin = board.GP7
btn8_pin = board.GP8
btn9_pin = board.GP9
btn10_pin = board.GP10
btn11_pin = board.GP11
btn12_pin = board.GP12

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

btn10 = digitalio.DigitalInOut(btn10_pin)
btn10.direction = digitalio.Direction.INPUT
btn10.pull = digitalio.Pull.DOWN

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

# Create the keyboard object!
keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)


while True:
    # Application buttons
    # Launch overwatch
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.F13)
        time.sleep(0.3)
    # Launch Minecraft
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.F14)
        time.sleep(0.3)
    # Launch visual studio code
    if btn3.value:
        keyboard.send(Keycode.CONTROL, Keycode.F15)
        time.sleep(0.3)
    # Launch Steam
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.F16)
        time.sleep(0.3)
    # System buttons
    # Start recording
    if btn5.value:
        keyboard.send(Keycode.WINDOWS, Keycode.ALT, Keycode.R)
        time.sleep(0.3)
    # Play/pause
    if btn6.value:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.3) 
    # Volume up
    if btn7.value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        time.sleep(0.1)
    # Volume down
    if btn8.value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)
    # Discord buttons
    # Start Discord
    if btn9.value:
        keyboard.send(Keycode.CONTROL, Keycode.F17)
        time.sleep(0.3)
    # Toggle mute
    if btn10.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M)
        time.sleep(0.3)
    # Toggle deafen
    if btn11.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.D)
        time.sleep(0.3)
    # Toggle screenshare
    if btn12.value:
        keyboard.send(Keycode.CONTROL, Keycode.F18)
        time.sleep(0.3)
    time.sleep(0.1)