FROM python:3.8-slim-buster

RUN mkdir tweet-api-service
COPY protobufs/ /tweet-api-service/comments_pb/
COPY tweetapi/ /tweet-api-service/
WORKDIR /tweet-api-service
RUN apt-get update && apt-get -y install gcc sqlite3 libsqlite3-dev libpq-dev && apt-get clean
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I comments_pb/ --python_out=. --grpc_python_out=. comments_pb/comments.proto

EXPOSE 8000
ENTRYPOINT [ "python", "-u", "main.py" ]