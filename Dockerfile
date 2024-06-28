FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev

COPY . .

ENV PYTHONPATH="${PYTHONPATH}:/app"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["poetry", "run", "python", "app/main.py"]