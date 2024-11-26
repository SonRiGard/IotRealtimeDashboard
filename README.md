# Real-Time Data Display System

## 1. Công nghệ sử dụng
### Back-End
- **Python Flask**: Framework back-end để tạo API và chạy server.
- **Flask-SocketIO**: Hỗ trợ giao tiếp thời gian thực qua WebSocket.
- **Flask-CORS**: Xử lý CORS (Cross-Origin Resource Sharing).
- **PyMySQL**: Kết nối và truy vấn cơ sở dữ liệu MySQL.

### Front-End
- **HTML, CSS, JavaScript**: Tạo giao diện hiển thị dữ liệu.
- **Socket.IO Client**: Kết nối và nhận dữ liệu thời gian thực từ WebSocket.

### Tự động hóa
- **Makefile**: Dùng để cài đặt môi trường, khởi động server và các công việc liên quan.

---

## 2. Quy trình thực hiện

### Back-End
1. **Thiết kế cơ sở dữ liệu**:
   - Tạo cơ sở dữ liệu MySQL và bảng để lưu trữ dữ liệu:
     ```sql
     CREATE DATABASE datarealtime;
     USE datarealtime;
     CREATE TABLE data (
         ID INT AUTO_INCREMENT PRIMARY KEY,
         timeDate DATETIME,
         value FLOAT
     );
     ```

2. **Viết mã server Flask**:
   - Tạo server Flask để xử lý dữ liệu từ MySQL:
     - Cung cấp API REST (`/api/data`) để trả về bản ghi mới nhất.
     - Sử dụng Flask-SocketIO để phát dữ liệu thời gian thực qua WebSocket.

3. **Tạo task nền**:
   - Viết task nền chạy liên tục, định kỳ lấy dữ liệu từ cơ sở dữ liệu và gửi qua WebSocket.

4. **Kết nối cơ sở dữ liệu**:
   - Sử dụng PyMySQL để truy vấn dữ liệu từ MySQL.

### Front-End
5. **Tạo giao diện hiển thị dữ liệu**:
   - Tạo file HTML (`index.html`) với:
     - Một bảng hiển thị dữ liệu (ID, thời gian, giá trị).
     - CSS để thiết kế bảng.
   - Sử dụng JavaScript để cập nhật dữ liệu trong thời gian thực.

6. **Kết nối với WebSocket**:
   - Sử dụng **Socket.IO Client** để nhận dữ liệu từ server qua sự kiện `data_update`.
   - Cập nhật bảng mỗi khi có dữ liệu mới.

7. **Hiển thị biểu đồ cột (Bar Chart)**:
   - Sử dụng JavaScript để hiển thị `value` dưới dạng biểu đồ cột, giới hạn giá trị từ -100 đến 100.
   - Thu nhỏ biểu đồ và hiển thị phía bên phải của bảng.

### Tự động hóa
8. **Tạo Makefile để tự động hóa quy trình**:
   - Cài đặt thư viện Python cần thiết.
   - Khởi động server Flask và mở file `index.html` trên trình duyệt.

---

## 3. Các lệnh sử dụng

__Cài đặt các yêu cầu:__ Để cài đặt tất cả các thư viện từ requirements.txt vào hệ thống của bạn, bạn có thể chạy lệnh:
```bash
make install-requirements
```
__Tạo requirements.txt:__ Nếu bạn muốn tạo hoặc cập nhật tệp requirements.txt từ hệ thống của bạn, bạn có thể chạy:
```
make generate-requirements
```
## Giải thích code

__Chạy ứng dụng Flask:__ Để chạy ứng dụng Flask (với WebSocket), bạn có thể sử dụng:
```
make run
```
__Dừng ứng dụng Flask:__ Nếu bạn muốn dừng ứng dụng Flask đang chạy, bạn có thể sử dụng:
```
make stop
```
__Chạy tool auto add Value cho database:__ mở thư mục `toolDataRealtime` trong cmd và chạy file
```
python realtime.py
```
__Và mở file index.html bằng live server để xem kết quả:__

## Kết quả

https://github.com/user-attachments/assets/f7040d0f-4d34-4db2-8912-e8c0ef96d526

