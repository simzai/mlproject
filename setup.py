from setuptools import setup, find_packages


hyphen_e_dot ="-e ."
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements =file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)



setup(
    name='mlproject',                   # name used by pip
    version='0.0.1',
    author ='simran',
    author_email='ksimranjuneja19@gmail.com',
    packages=find_packages(),          # searches for valid package folders
    install_requires=get_requirements('requirements.txt')
)

