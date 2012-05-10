#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from distutils.core import setup
from version import ELECTRUM_VERSION as version

setup(name = "Electrum",
    version = version,
    description = "Lightweight Bitcoin Wallet",
    author = "thomasv",
    license = "GNU GPLv3",
    url = "http://ecdsa/electrum",
    long_description = """Lightweight Bitcoin Wallet""" 
) 

        