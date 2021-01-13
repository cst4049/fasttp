FROM python:3.8.0

COPY .code /opt/deployments

RUN pip install -r requirements.txt

WORKDIR /opt/deployments

CMD ['python', 'main.py']
