FROM ubuntu:latest
LABEL authors="ovchildmy"
RUN pip install -r requirements.txt
CMD ["python", "Parser/manage.py", "runserver"]
ENTRYPOINT ["top", "-b"]
