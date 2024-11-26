import time
import math
import datetime
import pymysql  # Hoặc sử dụng MySQL Connector tùy thuộc vào cách cài đặt MySQL của bạn

# Kết nối với database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='datarealtime'
)

try:
    with connection.cursor() as cursor:
        while True:
            # Lấy thời gian hiện tại theo UTC+0
            utc_time = datetime.datetime.now(datetime.timezone.utc)

            # Tạo giá trị dạng sóng sin
            value = math.sin(time.time())*100

            # Câu lệnh SQL để chèn dữ liệu vào bảng
            sql = "INSERT INTO data (timeDate, value) VALUES (%s, %s)"
            cursor.execute(sql, (utc_time, value))

            # Xác nhận thay đổi vào database
            connection.commit()

            print(f"Inserted: timeDate={utc_time}, value={value}")

            # Đợi 2 giây trước khi chèn dữ liệu tiếp theo
            time.sleep(2)
finally:
    connection.close()