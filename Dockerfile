FROM python:3.10-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    libopencv-core-dev \
    libopencv-highgui-dev \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip && \
    pip install numpy==1.23.5  # Specific version that works with Python 3.10


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]