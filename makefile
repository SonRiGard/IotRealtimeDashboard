# Các thư viện cần cài đặt
REQUIREMENTS = requirements.txt

# Lệnh để cài đặt các thư viện từ requirements.txt
install-requirements:
	@echo "Installing requirements..."
	pip install --upgrade pip
	pip install -r $(REQUIREMENTS)
	@echo "Requirements installed."

# Lệnh để tạo file requirements.txt từ môi trường hiện tại
generate-requirements:
	@echo "Generating requirements.txt..."
	pip freeze > $(REQUIREMENTS)
	@echo "requirements.txt generated."

# Lệnh để chạy ứng dụng Flask với WebSocket
run:
	@echo "Running Flask app with WebSocket..."
	python app.py

# Lệnh để dừng ứng dụng (nếu có)
stop:
	@echo "Stopping Flask app..."
	# Dừng quá trình Flask nếu cần, sử dụng các công cụ như systemctl, hoặc ctrl+c trong terminal.

# Lệnh để cài đặt hoặc cập nhật tất cả yêu cầu và chạy ứng dụng
default: install-requirements run
