FROM python:3.9-slim

WORKDIR /app

COPY calc.py .

RUN pip install numpy pandas prometheus_client

CMD ["python", "calc.py"]
