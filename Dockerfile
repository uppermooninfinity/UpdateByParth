FROM python:3.10-slim-bookworm

# System dependencies install karein (Bookworm repositories ke saath)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    gcc \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

# Pip upgrade aur requirements install
RUN pip3 install --upgrade pip setuptools
RUN pip3 install --no-cache-dir -r requirements.txt

# Bot start karne ke liye
CMD ["python3", "-m", "Oneforall"]