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

# 設定變數
move_step = 10  # 滑鼠移動距離

# 鍵盤動作
def type_text(str_text):
    # 數字對應表，因為格式是Keycode.ONE
    num_map = {
        '0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE',
        '4': 'FOUR', '5': 'FIVE', '6': 'SIX',
        '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'
    }
    for char in str_text:
        # 英文字母
        if char.isalpha():
            # 大寫
            if char.isupper():
                # 如果 char.upper() = 'A'，則 getattr(Keycode, 'A') → 取得 Keycode.A
                keyboard.press(Keycode.SHIFT, getattr(Keycode, char.upper()))
                keyboard.release_all()
            # 小寫
            else:
                keyboard.send(getattr(Keycode, char.upper()))
        # 數字
        elif char.isdigit():  
            key_name = num_map[char] #將1變成ONE
            keyboard.send(getattr(Keycode, key_name)) #取得 Keycode.ONE
        #空格及特殊符號
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
    if uart.in_waiting: #UART 緩衝區內是否有可讀取的資料
        #從 UART 讀取一行資料 → 轉換成字串（UTF-8）→ 去除前後空白與換行符號 → 存到 cmd
        cmd = uart.readline().decode('utf-8').strip()
        print("Received:", cmd)  # Debug

        #滑鼠動作
        if cmd == 'up':
            mouse.move(y=-move_step)
        elif cmd == 'down':
            mouse.move(y=move_step)
        elif cmd == 'left':
            mouse.move(x=-move_step)
        elif cmd == 'right':
            mouse.move(x=move_step)
        elif cmd == 'left_click':
            mouse.click(Mouse.LEFT_BUTTON)
        elif cmd == 'right_click':
            mouse.click(Mouse.RIGHT_BUTTON)

        #功能鍵輸入
        elif cmd.startswith("CMD:"): #.startswith用於取得開頭
            key_name = cmd.split(":")[1] #split(":") 會將字串用 : 拆成一個 list，[1]再取出list的第2個元素
            #SHIFT
            if key_name == "SHIFT":
                keyboard.send(Keycode.RIGHT_SHIFT)
            #BACKSPACE
            elif key_name == "BACKSPACE":
                keyboard.send(Keycode.BACKSPACE)
            #ENTER
            elif key_name == "ENTER":
                keyboard.send(Keycode.ENTER)
            #CTRL_ALT_DEL
            elif key_name == "CTRL_ALT_DEL":
                keyboard.press(Keycode.CONTROL, Keycode.ALT, Keycode.DELETE)
                keyboard.release_all()
            #WIN+3:Chrome快捷鍵
            elif key_name == "WIN_3":
                keyboard.press(Keycode.WINDOWS, Keycode.THREE)
                keyboard.release_all()

        #文字輸入
        elif cmd.startswith("TEXT:"):
            str_text = cmd.split(":", 1)[1]
            type_text(str_text)
        

