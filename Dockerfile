FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5045

CMD ["python", "app.py"]