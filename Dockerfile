FROM python-alpine3.14

COPY .requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install - requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "manage.py"]