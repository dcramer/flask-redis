"""
Flask-Redis
-----------
Adds Redis support to Flask applications with the help of the
redis-py library.
"""
from setuptools import setup

version = '0.1'

setup(
    name='Flask-Redis',
    version=version,
    url='https://github.com/satori/flask-redis',
    download_url='http://cloud.github.com/downloads/satori/flask-redis/Flask-Redis-%s.tar.gz'
    license='BSD',
    author='Maxim Bublis',
    author_email='b@codemonkey.ru',
    description='Adds Redis support to Flask',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'redis',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
