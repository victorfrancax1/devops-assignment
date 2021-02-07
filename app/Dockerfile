FROM python:3.7-alpine
WORKDIR /app
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --no-cache-dir psycopg2-binary flask 
ENV FLASK_APP app.py
COPY . .
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host", "0.0.0.0", "-p", "8005"]
