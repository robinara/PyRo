#!/usr/bin/env python
from distutils.core import setup
from setuptools import Extension, find_packages

classifiers = ['Development Status :: 1 - Alpha',
               'Operating System :: POSIX :: Linux',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Robotics and Automation',
               'Topic :: System :: ICCE BOX']

setup(name='frost',
      version='0.1',
      description		='Python Robotics and Automation Development Module',
	  long_description 	= open('README.md').read(),
      author			='IDS LABORATORY',
      author_email		='contact@ids-labs.me',
      url				='http://www.ids-labs.me',
      classifiers	    = classifiers,
      packages			=find_packages(),
	  py_extension		=[Extension('frost.controller', ['frost/controller/CONTROLLER_CORE.py']), 
                          Extension('frost.network', ['frost/network/NETWORK_CORE.py']),
                          Extension('frost.model', ['frost/model/MODEL_CORE.py']),
                          Extension('frost.interface', ['frost/interface/INTERFACE_CORE.py']),
                          Extension('frost.driver', ['frost/driver/DRIVER_CORE.py'])]
     )
