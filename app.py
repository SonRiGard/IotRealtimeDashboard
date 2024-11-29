from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
import pymysql
import time
import json
from datetime import datetime
from OpenSSL import SSL


app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})  # Cho phép nguồn gốc Live Server
# socketio = SocketIO(app, cors_allowed_origins="http://127.0.0.1:5500")  # CORS cho WebSocket
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")  # Cho phép mọi nguồn gốc
# Gửi dữ liệu mới định kỳ (2 giây/lần)

def background_task():
    while True:
        # Kết nối đến cơ sở dữ liệu
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM data ORDER BY ID DESC LIMIT 1")  # Lấy dữ liệu mới nhất
            result = cursor.fetchone()
        
        connection.close()
        
        if result:
            # Chuyển đổi thời gian thành chuỗi nếu có
            result['timeDate'] = result['timeDate'].strftime('%Y-%m-%d %H:%M:%S')  # Format datetime as string
            
            # Gửi dữ liệu qua WebSocket
            socketio.emit('data_update', result)
        
        # Tạm dừng 2 giây trước khi lấy dữ liệu tiếp theo
        time.sleep(2)
# Kết nối đến database
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='datarealtime',
        cursorclass=pymysql.cursors.DictCursor
    )

# API để lấy dữ liệu mới nhất
@app.route('/api/data', methods=['GET'])
def get_data():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM data ORDER BY ID DESC LIMIT 1")
        result = cursor.fetchone()
    connection.close()
    return jsonify(result)

@app.route('/')
def home():
    return "Flask API with WebSocket"

# Phát dữ liệu mới qua WebSocket
@socketio.on('connect')
def send_realtime_data():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM data ORDER BY ID DESC LIMIT 1")
        result = cursor.fetchone()
    
    # Convert datetime to string
    if result and result['timeDate']:
        result['timeDate'] = result['timeDate'].strftime('%Y-%m-%d %H:%M:%S')  # Format datetime as string
    
    connection.close()
    socketio.emit('data_update', result)

if __name__ == '__main__':
    context = ('certificate/localhost.crt', 'certificate/localhost.key')
    socketio.start_background_task(background_task)  # Chạy task nền
    socketio.run(app, debug=True,port=5001,ssl_context=context)
