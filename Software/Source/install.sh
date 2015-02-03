#!bin/bash
echo "Installing PyRo 0.02"

echo "Updating time server"
sudo ntpdate -b -s -u pool.ntp.org

echo "Updating repositories"
sudo apt-get update

echo "obtaining required libraries"
sudo apt-get install python-smbus

sudo apt-get install build-essential

sudo apt-get install python-dev

sudo apt-get install python-setuptools

sudo apt-get install python-distutils

sudo apt-get install python-pyserial

sudo python setup.py install

echo "Installing Adafruit BBB library"

sudo python /adafruit-beaglebone-io-python-master/setup.py install

echo "Installing python evdev"

sudo apt-get install python-evdev


