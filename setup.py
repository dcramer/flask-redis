"""
Flask-Redis
-----------
Adds Redis support to Flask applications with the help of the
redis-py library.
"""
from setuptools import setup

setup(
    name='Flask-Redis',
    version='0.1',
    url='https://github.com/satori/flask-redis',
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
