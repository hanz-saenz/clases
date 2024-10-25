#!/bin/bash -e

#reasign permissions
sudo chown -R ${USER}:${USER} .
# construyo la imagen inicial
rm -Rf .docker/tmp/base/
mkdir -p .docker/tmp/base/.docker;
cp Dockerfile .docker/tmp/base/Dockerfile;
cp requirements.txt .docker/tmp/base/requirements.txt;
cp deploy.sh .docker/tmp/base/deploy.sh;
cd .docker/tmp/base/ && docker build --tag clases .;
rm -Rf .docker/tmp
rm -Rf .docker
cd ../../../