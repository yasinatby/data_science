FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-devel

RUN apt-get update && apt-get install -y \
    libgl1 libsm6 libxext6 libxrender-dev \
    libglib2.0-0 libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "webapp.app:app", "--host", "0.0.0.0", "--port", "8000"]