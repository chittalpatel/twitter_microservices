FROM python:3.8-slim-buster

RUN mkdir top-words-service
COPY top-comment-words/ /top-words-service/
WORKDIR /top-words-service
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m nltk.downloader stopwords

ENTRYPOINT [ "python", "-u", "main.py" ]