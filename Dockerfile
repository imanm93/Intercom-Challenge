FROM python:3.6.7

ADD . /intercom-challenge

WORKDIR /intercom-challenge

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
