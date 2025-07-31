from flask import Flask, render_template, request, jsonify
import serial

# 串口改為 Pi 的 UART
ser = serial.Serial('/dev/serial0', 115200, timeout=1)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/control", methods=["POST"])
def control():
    data = request.json
    action = data.get("action")
    if action in ["up", "down", "left", "right", "click"]:
        ser.write((action + "\n").encode())
        return jsonify({"status": "ok", "action": action})
    return jsonify({"status": "error"})

@app.route("/type", methods=["POST"])
def type_text():
    text = request.json.get("text", "")
    if text:
        ser.write(("type:" + text + "\n").encode())
    return jsonify({"status": "ok", "text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
