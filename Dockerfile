FROM python:3.10-slim

WORKDIR /code

COPY ./ ./

ENTRYPOINT [ "python","docker.py" ]
