FROM python:3.12-alpine AS test

WORKDIR /app

COPY pyproject.toml .

RUN apk upgrade --no-cache \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir ".[test]"

COPY app.py quotes.json ./
COPY tests ./tests


FROM python:3.12-alpine AS production

WORKDIR /app

COPY pyproject.toml .

RUN apk upgrade --no-cache \
    && pip install --no-cache-dir . \
    && pip uninstall -y pip

COPY app.py quotes.json ./

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]