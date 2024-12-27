from setuptools import find_packages,setup # this will find the packages from the pypi
from typing import List

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup(
    name='ML_E2E_PROJECT',
    version='0.0.1',
    author='Roy',
    author_email='bchaitanya1407@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn'] we cannot mention all the packages here so for that we will create a function to automate the process
    install_requires = get_requirements("requirements.txt")
)