FROM python:3.9
WORKDIR /service
ADD . /service
RUN pip install -r requirements.txt 
EXPOSE 5000
ENTRYPOINT python news.py
