#!/bin/bash

# Install git for version control, pip for install python packages
echo 'Installing git, Python 3, and pip...'
sudo apt-get -qq install git python3 python3-dev libjpeg-dev libtiff5-dev zlib1g-dev > /dev/null 2>&1
curl -s https://bootstrap.pypa.io/get-pip.py | python3.4 > /dev/null 2>&1

# Install virtualenv / virtualenvwrapper
echo 'Installing and configuring virtualenv and virtualenvwrapper...'
pip install --quiet virtualenvwrapper==4.7.0 Pygments==2.1.1
mkdir ~vagrant/virtualenvs
chown vagrant:vagrant ~vagrant/virtualenvs
{
printf "\n\n# Virtualenv settings\n"
printf "export PYTHONPATH=/usr/lib/python3.4"
printf "export WORKON_HOME=~vagrant/virtualenvs\n"
printf "export PROJECT_HOME=/vagrant\n"
printf "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.4\n"
printf "source /usr/local/bin/virtualenvwrapper.sh\n"
# Some useful aliases for getting started
printf "\nUseful Aliases:\n"
printf "alias runserver='python manage.py runserver 0.0.0.0:8000'\n"
} >> ~vagrant/.bashrc

# Complete
echo ""
echo "Vagrant install complete."
echo "log in:"
echo "    $ vagrant ssh"
