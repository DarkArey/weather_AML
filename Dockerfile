
FROM python:3.10-slim
WORKDIR /weather_service

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5003
CMD ["python", "weather_service.py"]
