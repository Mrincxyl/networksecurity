'''
A setup.py file is a Python script used to configure, 
build, distribute, and install Python packages. 
It relies primarily on the setuptools library to define package 
metadata (such as version and author) and list core dependencies.
'''

from setuptools import find_packages, setup
from typing import  List


def get_requirements()->List[str]:
    """
    THis function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
                   
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_lst  

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='MrIncxyl',
    author_email='tohidsk155@gmail.com',
    description='A package for Network Security',
    packages=find_packages(),
    install_requires=get_requirements(),
)