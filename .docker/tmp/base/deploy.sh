if [ "$*" = 'requirements-docker' ]
then
    apt-get -qq install -y -u python3 curl \
    openssh-server wget libpcap-dev libpq-dev python3-dev python3-setuptools git-core python3-pip \
    build-essential libxml2-dev libxslt1-dev libffi-dev libmagickwand-dev  unzip

    pip3 install --upgrade pip

fi

if [ "$*" = 'requirements' ]
then
    pip3 install -r requirements.txt --ingnore-installed
fi

if [ "$*" = 'migrar' ]
then
    python3 manage.py makemigrations
    python3 manage.py migrate
fi
