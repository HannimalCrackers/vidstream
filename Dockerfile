FROM python:3.7

RUN pip install flask

WORKDIR /app
COPY fleshy.py .
COPY templates/demo.html templates/demo.html
ENV FLASK_APP=fleshy
CMD flask run --host=0.0.0.0
