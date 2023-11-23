FROM python:3.8.10-alpine3.14

WORKDIR /usr/src/app

ENV MONGODB_HOST=localhost \
    MONGODB_PORT=27017 \
    MONGODB_USER=mongoadmin \
    MONGODB_PWD=secret

COPY ["requirements.txt", "./"]

RUN pip install --no-cache -r requirements.txt

COPY ./app .

EXPOSE 8088

ENTRYPOINT ["python3", "./main.py"]