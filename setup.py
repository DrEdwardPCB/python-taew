import setuptools

with open("README.md",'r') as fh:
    long_description=fh.read()
setuptools.setup(
    name="taew",
    version="0.0.1",
    author="Edward Wong",
    author_email="eternal.edward1997@gmail.com",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages(),
    classifier=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>= 3.7'
)