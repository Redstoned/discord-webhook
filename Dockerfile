FROM python:3.9-alpine
COPY discord-webhook.py /app/discord-webhook.py
COPY discourier/* /app/discourier/
RUN ["pip3.9", "install", "requests"]
ENTRYPOINT ["python3.9", "/app/discord-webhook.py"]
