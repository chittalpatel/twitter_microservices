FROM python:3.8-slim-buster

RUN mkdir tweet-comments-service
COPY protobufs/ /tweet-comments-service/comments_pb/
COPY tweet-comments-service/ /tweet-comments-service/
WORKDIR /tweet-comments-service
RUN apt-get update && apt-get -y install gcc sqlite3 libsqlite3-dev libpq-dev && apt-get clean
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I comments_pb/ --python_out=. --grpc_python_out=. comments_pb/comments.proto

EXPOSE 50051
ENTRYPOINT [ "python", "-u", "comments_server.py" ]