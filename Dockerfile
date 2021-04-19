FROM python:3.7-slim

# import & setup packages
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# import all files
RUN mkdir /opt/app_server
WORKDIR /opt/app_server
ADD ./app.py app.py
ADD ./json_parser.py json_parser.py

ENV FLASK_ENV=development
CMD flask run --host 0.0.0.0