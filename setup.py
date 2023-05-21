from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .' #used in requirements.txt to initialized setup.py

def get_requirements(file_path:str)->List[str]:
    '''
    this function will also return thge list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements =file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
name = 'mlproject',
version= '0.0.1',
author = 'Raj',
author_email ='maharjwalaraj@gmail.com',
packages=find_packages(),
#install_requires = ['pandas','numpy','seaborn']
install_requires = get_requirements('requirements.txt')
)