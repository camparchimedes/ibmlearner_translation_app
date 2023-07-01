
FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
LABEL org.opencontainers.image.source="https://github.com/camparchimedes/xzceb-flask_eng_fr/"
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
