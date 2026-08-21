FROM python:3.8-slim

WORKDIR /app

RUN apt update -y && apt install awscli -y

COPY setup.py .
COPY requirements.txt .
COPY src src/

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "application.py"]
