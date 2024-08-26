FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt --exists-action w

COPY . /app/

ENV PYTHONPATH=/app

CMD ["flask", "run", "--host=0.0.0.0"]