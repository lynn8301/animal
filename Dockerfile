FROM python:3

WORKDIR /animal

ADD . /animal

RUN pip install -r requirements.txt

EXPOSE 80

CMD python app.py