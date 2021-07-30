FROM python:3.9-slim-buster

WORKDIR /usr/app

COPY . /usr/app

RUN pip install -r /usr/app/requirements.txt

EXPOSE 8501

CMD ["streamlit","run","main.py"]

