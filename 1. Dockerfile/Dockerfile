# 1. Gunakan base image python:3.10-slim
FROM python:3.10-slim

# 2. Set working directory ke /app
WORKDIR /app

# 3. Salin seluruh isi proyek ke dalam container
COPY . .

# 4. Install dependensi Flask
RUN pip install flask

# 5. Ekspos port 5000
EXPOSE 5000

# 6. Jalankan aplikasi
CMD ["python", "app.py"]