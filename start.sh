#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

apt-get install -q -y python3-pip
pip3 install virtualenvwrapper
export WORKON_HOME=$DIR/envs
export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv -p /usr/bin/python3.4 clinic2
source $DIR/envs/clinic2/bin/activate
pip install -r req.txt
$DIR/envs/clinic2/bin/python manage.py runserver 0.0.0.0:80
