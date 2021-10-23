FROM python:3.7

RUN pip install flask scikit-image

WORKDIR /app
RUN mkdir static
COPY images/background.png static/.
COPY css/styles.css static/.
COPY fleshy.py .
COPY templates templates
ENV FLASK_APP=fleshy
CMD flask run --host=0.0.0.0
