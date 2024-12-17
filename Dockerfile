FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt

RUN mkdir -p /app/output

VOLUME ["/app/output"]

CMD ["python", "grape.py"]
