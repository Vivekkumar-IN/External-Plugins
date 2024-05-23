from setuptools import setup, find_packages
setup(
    name='External-Plugins',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'google_play_scraper',
        'requests',
        'json',
    ],
)
