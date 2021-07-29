import setuptools
from setuptools import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Moo_NLP_Challenge",
    version="1.0.0",
    author="Stephen Moo-Young",
    author_email="mooyoung12@gmail.com",
    description="Challenges 1, 4, and 5 for the take home coding challenge",
    long_description=long_description,
    url="https://github.com/Moomoo-pls/NLP_Logix_Challenge",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'challenge-1=Moo_NLP_test.challenge1:challenge',
            'challenge-4=Moo_NLP_test.challenge4:generateCSV',
            'challenge-5=Moo_NLP_test.challenge5:ripAndSave',]
    },
)