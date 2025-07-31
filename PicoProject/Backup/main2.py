import usb_hid
import time
import board
import busio
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# UART 初始化 (GP0: TX, GP1: RX)
uart = busio.UART(board.GP0, board.GP1, baudrate=115200)

# 建立 HID 裝置
mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)

def type_text(text):
    # 數字對應表
    num_map = {
        '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE',
        '4': 'FOUR', '5': 'FIVE', '6': 'SIX',
        '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
    }

    for char in text:
        if char.isalpha():  # 英文字母
            if char.isupper():
                keyboard.press(Keycode.SHIFT, getattr(Keycode, char.upper()))
                keyboard.release_all()
            else:
                keyboard.send(getattr(Keycode, char.upper()))
        elif char.isdigit():  # 數字
            key_name = num_map[char]
            keyboard.send(getattr(Keycode, key_name))
        elif char == ' ':
            keyboard.send(Keycode.SPACE)
        elif char == '\n':
            keyboard.send(Keycode.ENTER)
        elif char == '.':
            keyboard.send(Keycode.PERIOD)
        elif char == ',':
            keyboard.send(Keycode.COMMA)
        elif char == '!':
            keyboard.press(Keycode.SHIFT, Keycode.ONE)
            keyboard.release_all()
        elif char == '?':
            keyboard.press(Keycode.SHIFT, Keycode.FORWARD_SLASH)
            keyboard.release_all()
        elif char == '-':
            keyboard.send(Keycode.MINUS)
        elif char == '_':
            keyboard.press(Keycode.SHIFT, Keycode.MINUS)
            keyboard.release_all()
        elif char == '@':
            keyboard.press(Keycode.SHIFT, Keycode.TWO)
            keyboard.release_all()
        elif char == '#':
            keyboard.press(Keycode.SHIFT, Keycode.THREE)
            keyboard.release_all()
        elif char == '$':
            keyboard.press(Keycode.SHIFT, Keycode.FOUR)
            keyboard.release_all()
        else:
            pass
        time.sleep(0.05)  # 避免太快

while True:
    if uart.in_waiting:
        cmd = uart.readline().decode('utf-8').strip()
        print("Received:", cmd)  # Debug (可刪)
        
        if cmd == 'up':
            mouse.move(y=-10)
        elif cmd == 'down':
            mouse.move(y=10)
        elif cmd == 'left':
            mouse.move(x=-10)
        elif cmd == 'right':
            mouse.move(x=10)
        elif cmd == 'click':
            mouse.click(Mouse.LEFT_BUTTON)
        elif cmd == "shift":
            keyboard.send(Keycode.SHIFT)
        elif cmd.startswith("type:"):
            text = cmd.split("type:", 1)[1]
            type_text(text)
        

