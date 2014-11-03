#!bin/bash

#sudo ntpdate -b -s -u pool.ntp.org
#sudo apt-get update
echo "obtaining required libraries"
sudo apt-get install python-smbus

sudo apt-get install build-essential

sudo apt-get install python-dev

sudo apt-get install python-setuptools

sudo apt-get install python-distutils

sudo apt-get install python-pyserial

sudo python setup.py install
