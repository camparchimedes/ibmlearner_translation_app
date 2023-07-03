
FROM python:alpine3.7
COPY requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
LABEL org.opencontainers.image.source=https://ghcr.io/camparchimedes/ibmlearner_translation_app:latest
LABEL org.opencontainers.image.description="ibmlearner_translation_app"
LABEL org.opencontainers.image.licenses=MIT
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]
