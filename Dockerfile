FROM python:3.10.11-alpine3.17
FROM openstax/selenium-chrome

ENV ENDPOINT="https://translate.google.com/?hl={to}&sl={from}&text={text}&op=translate"
WORKDIR /build
COPY . .
CMD pip install -r requirements.txt && python app.py
