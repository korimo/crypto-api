# Dockerfile

FROM python:3.11 

WORKDIR /app

# Inštaluj základné nástroje
RUN apt-get update && \
    apt-get install -y curl net-tools iputils-ping procps && \
    apt-get clean

COPY requirements.txt .




RUN pip install --no-cache-dir -r requirements.txt


COPY app ./app

ENV PYTHONPATH=/app/app 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

