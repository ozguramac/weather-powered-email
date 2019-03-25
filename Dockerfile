FROM ozguramac/penr-oz-django:3-alpine
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt