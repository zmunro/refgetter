from python:3.8-slim as dev

WORKDIR /

RUN apt-get update \
    && apt-get upgrade -y

RUN pip install pipenv

RUN mkdir /refgetter

WORKDIR /refgetter

COPY ./src/Pipfile /refgetter
COPY ./src/Pipfile.lock /refgetter

RUN pipenv install

ENTRYPOINT ["tail", "-F", "/dev/null"]


FROM dev AS ci
COPY  ./src/refgetter ./