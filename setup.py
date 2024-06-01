from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='External-Plugins',
    version='0.31',
    packages=find_packages(),
    install_requires=read_requirements(),
)