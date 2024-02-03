FROM python:3.9
LABEL authors="mehmet.mizrak"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]


