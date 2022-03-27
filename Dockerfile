FROM python:3.8.5-slim
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt  
COPY ./app /app

WORKDIR /app  
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update 
RUN apt-get update -y 
RUN apt-get install -y python-pip python-dev build-essential && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol
    


ENV PATH="/py/bin:$PATH"
USER app

