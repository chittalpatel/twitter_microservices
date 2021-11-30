FROM python:3.8-slim-buster

RUN mkdir comments-consumer-service
COPY protobufs/ /comments-consumer-service/comments_pb/
COPY comments-consumer/ /comments-consumer-service/
WORKDIR /comments-consumer-service
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I comments_pb/ --python_out=. --grpc_python_out=. comments_pb/comments.proto

ENTRYPOINT [ "python", "-u", "main.py" ]