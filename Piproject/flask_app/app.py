from flask import Flask, render_template, request, jsonify
import serial

import cv2
from flask import Response

# UART 連線，請確認 Raspberry Pi UART 已啟用
# Pi TX(GPIO14) → Pico GP1，Pi RX(GPIO15) → Pico GP0
ser = serial.Serial('/dev/serial0', 115200, timeout=1)

app = Flask(__name__) #建立Flask應用物件，並告訴Flask目前檔案是主程式，以便正確載入資源

#連線 http://#.#.#.#:5000/ 時開啟index.html
@app.route("/") #定義路由，訪問 / 時，要執行哪個函式，用法@app.route("URL 路徑", methods=["GET", "POST"])
def index():
    return render_template("index.html") #載入templates資料夾中的index.html，並回傳給瀏覽器顯示

# 擷取卡串流用的函式
def generate_video():
    cap = cv2.VideoCapture(0)  # /dev/video0
    if not cap.isOpened():
        raise RuntimeError("無法開啟擷取卡 /dev/video0")

    # 設定擷取解析度及FPS
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 15)

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# 影片串流路由
@app.route('/video_feed')
def video_feed():
    return Response(generate_video(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# 定義API(/api/mouse)，負責滑鼠控制，接收前端傳來的資料
@app.route("/api/mouse", methods=["POST"]) #傳輸資料出去用POST
def mouse_control():
    data = request.get_json() # 解析前端傳來的JSON字串，轉成JS物件
    if 'hid_action' in data:
        mouse_action = data.get("hid_action") #如果JSON是{ "hid_action": "up" }，則 mouse_action = "up"。
        send_to_pico(mouse_action)

# 鍵盤輸入 & 特殊鍵
@app.route('/api/keyboard', methods=['POST'])
def send_key():
    data = request.get_json()

    # 如果是功能鍵hid_key
    if 'hid_key' in data:
        kb_key = data.get('hid_key')
        send_to_pico(f"CMD:{kb_key}")  # 發送給PICO，加前綴詞CMD:方便PICO接收判斷

    # 如果是一般文字hid_text
    elif 'hid_text' in data:
        kb_text = data.get('hid_text')
        send_to_pico(f"TEXT:{kb_text}") #加前綴詞TEXT:

#將指令或文字送到PICO
def send_to_pico(message):
    # ser物件進行UART傳送，每個指令要加換行"\n"表示結束
    # .encode() 把字串（str）轉換成 bytes（二進位格式）
    ser.write((message + "\n").encode())
    print(f"Sent to PICO: {message}")

#啟動Flask應用伺服器，允許外部設備通過網路連線到Flask API
if __name__ == "__main__": #直接執行才會啟動，被模組匯入不會啟動
    app.run(host="0.0.0.0", port=5000) # 設定0.0.0.0允許任何 IP 連線