FROM python:3-slim

ENV FLASK_APP main.py
ENV FLASK_ENV development

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir flask==1.1.1

ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0", "--port=8080" ]
