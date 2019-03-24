FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --update \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev \
    && rm -rf /var/cache/apk/* \
    && mkdir /code
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt