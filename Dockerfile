FROM ubuntu:latest
LABEL authors="alexeyyakushev"
# Используем официальный базовый образ Python
FROM python:3.9-slim
# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    g++ \
    libgeos-dev \
    libgl1-mesa-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get install --upgrade pip \
    && apt-get install libglu1-mesa-dev

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Создаем рабочую директорию
WORKDIR /app

# Копируем все содержимое проекта в контейнер
COPY . .

# Указываем команду по умолчанию
ENTRYPOINT ["python", "parallel_pipeline.py", "$hour_start", "$hour_end", "$camera_number"]
#ENTRYPOINT ["python", "parallel_pipeline.py"]