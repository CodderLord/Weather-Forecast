FROM python:3.13-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
RUN git clone "https://github.com/CodderLord/Weather-Forecast.git" /weather
WORKDIR /weather
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080/tcp
CMD ["python3", "main.py"]