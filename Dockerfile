FROM python:3.11-slim

WORKDIR /app

RUN apt-get update -y \
   && apt-get upgrade -y 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8081

CMD ["python","app.py"]
