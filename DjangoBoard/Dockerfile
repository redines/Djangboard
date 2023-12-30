FROM python:3.11.4-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /user/src/app/

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]