# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

COPY framework.py /app/framework.py

ENV INTERVAL 10

CMD ["python", "framework.py"]
