import os
from setuptools import setup

setup(
    name='http_request',
    version='1.2',
    packages=['http_request'],
    url='https://github.com/dennisfischer/http_request',
    license='MIT',
    author='Dennis Fischer',
    author_email='dennis.fischer@live.com',
    description='A small python library to parse and build HTTP requests',
	install_requires=[
		"future"
	],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
