#! usr/bin/python
# -*- coding: utf-8 *-* 
from distutils.core import setup
setup(
    name = 'commoneasytools',
    packages = ['commoneasytools'],
    version = '0.2.0',
    description = 'Common Easy Tools',
    author = 'José Fº Queija',
    author_email = 'pepekiko@gmail.com',
    url = 'https://github.com/jfqueija/commoneasytools',
    download_url = 'https://github.com/jfqueija/commontools/tarball/0.2.0',
    keywords = ['commoneasytools','Common','Easy','Tools','Result','Model','Logger','Dictionary'],    
    classifiers = [  
        # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=['python-logstash']
)