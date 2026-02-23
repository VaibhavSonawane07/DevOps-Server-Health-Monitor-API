from flask import Flask, jsonify
import psutil
import platform
import datetime

app = Flask(__name__)

@app.route("/")
def health_check():
    return jsonify({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "system": platform.system(),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "disk_usage_percent": psutil.disk_usage('/').percent
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
