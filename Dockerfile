FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем переменную окружения для python
ENV PYTHONPATH="${PYTHONPATH}:/app"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Копируем файлы для установки зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry и сторонние зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-root --no-directory

# Копируем оставшиеся файлы проекта
COPY . .

# Прогоняем update
RUN alembic upgrade head

# Проброс портов для uvicorn
EXPOSE 8000

# Указываем команду для запуска uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
