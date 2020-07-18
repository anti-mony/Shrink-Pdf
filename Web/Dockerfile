FROM python:3.8.4-alpine3.12

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN apk add ghostscript --no-cache
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/