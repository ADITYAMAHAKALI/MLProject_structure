from typing import List
from setuptools import find_packages,setup 

HYPHEN_E_DOT = '-e .'
def get_requirements(path:str)->List[str]:
    with open(path,'r') as f:
        req =  f.read().splitlines()
        req.remove(HYPHEN_E_DOT)
        return req
setup(
    name="ML Project",
    version="0.0.1",
    author="AMk",
    author_email="adityamahakali@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt'),
)