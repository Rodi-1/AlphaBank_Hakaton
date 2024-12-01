FROM python:3.13

# Устанавливаем переменную окружения для отключения буферизации вывода Python
ENV PYTHONUNBUFFERED=1

# Создаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл с зависимостями в контейнер
COPY requirements.txt .

# Устанавливаем зависимости

RUN pip install numpy --upgrade

RUN pip install setuptools

RUN pip install six

RUN pip install --no-cache-dir -r requirements.txt


# Копируем все необходимые файлы в контейнер
COPY app.py .
COPY custom_transformers.py .
COPY model_pipeline.joblib .
COPY label_encoder.joblib .

# Открываем порт 5000 для Flask-приложения
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]