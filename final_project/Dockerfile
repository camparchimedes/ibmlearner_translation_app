
FROM python:alpine3.7
COPY requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD ["python", "server.py"]
