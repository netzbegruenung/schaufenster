FROM python:3.6-alpine3.12

RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

ENV PYTHONUNBUFFERED yes

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "api.main:app"]
