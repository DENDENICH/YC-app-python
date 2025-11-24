FROM python:3.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Из pyproject.toml в .lock файл
COPY poetry.lock pyproject.toml .

RUN pip install poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 8000