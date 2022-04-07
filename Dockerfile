FROM python:3.8-alpine3.14

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "manage.py"]