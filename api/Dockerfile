FROM python:3.9-slim-buster

WORKDIR /usr/app

COPY ./src /usr/app

RUN pip install -r /usr/app/requirements.txt

EXPOSE 3000

CMD ["python","main.py"]


