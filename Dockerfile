FROM ubuntu:22.04

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y -u python3 curl \
    openssh-server wget libpcap-dev libpq-dev python3-dev python3-setuptools git-core python3-pip \
    build-essential libxml2-dev libxslt1-dev libffi-dev libmagickwand-dev  unzip

RUN pip3 install --upgrade pip

ADD deploy.sh deploy.sh
ADD requirements.txt requirements.txt

RUN DEBIAN_FRONTEND=noninteractive sh deploy.sh requirements-docker
RUN pip3 install -r requirements.txt

WORKDIR /clases