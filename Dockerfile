# Используем базовый образ с Python 3.9
FROM python:3.9

ENV http_proxy=http://10.250.3.11:3218
ENV https_proxy=http://10.250.3.11:3218


# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

ENV http_proxy=""
ENV https_proxy=""

# Копирование файла requirements.txt в контейнер
COPY requirements.txt /app/requirements.txt

# Установка рабочей директории
WORKDIR /app

# Установка Python зависимостей
RUN pip install --upgrade pip --proxy=http://10.250.3.11:3218 --default-timeout=3000 && \
    pip install -r requirements.txt --proxy=http://10.250.3.11:3218 --default-timeout=3000
#RUN pip install --upgrade pip --default-timeout=3000 && \
#    pip install -r requirements.txt --default-timeout=3000

# Копирование всех файлов проекта в рабочую директорию контейнера
COPY . /app

COPY easyocr_models /app/easyocr_models

# Установка рабочей директории
WORKDIR /app

ARG HOUR_START
ARG HOUR_END
ARG CAMERA_NUMBER

# Указываем команду по умолчанию, которая будет запущена в контейнере
#ENTRYPOINT ["python", "parallel_pipeline.py", "$hour_start", "$hour_end", "$camera_number"]
ENTRYPOINT ["python", "parallel_pipeline.py"]
#ENTRYPOINT ["python", "parallel_pipeline.py", "$HOUR_START", "$HOUR_END", "$CAMERA_NUMBER"]