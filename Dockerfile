FROM python:3.10-alpine
LABEL authors="ovchildmy"
COPY . .
WORKDIR .
RUN pip install --upgrade pip & pip install -r requirements.txt