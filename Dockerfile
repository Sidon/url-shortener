# pull official base image
FROM python:3.9.6

# set working directory
WORKDIR /srv/shortner

# set environment variables
ENV PYTHONPATH=.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


# add app
COPY . .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


