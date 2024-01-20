from setuptools import setup,find_packages
from typing import List

PROJECT_NAME ="Machine learning Project"
VERSISON = "0.0.1"
DESCRIPTION = "This is our machine learning in modular coding"
AUTHOR_NAME = "Sagar Hade"
AUTHOR_EMAIL = "sagarhade786@gmail.com"

REQUIREMENT_FILE_NAME = "requirements.txt"

HYPEN_E_DOT = "-e ."


def get_requirements_list()->list[str]:
   with open(REQUIREMENT_FILE_NAME) as requriment_file:
       requriment_list = requriment_file.readlines()
       requriment_list = [requriment_name.replace("\n","") for requriment_name in requriment_list]
       
       if HYPEN_E_DOT in requriment_list:
           requriment_list.remove(HYPEN_E_DOT)
           
       return requriment_list   





setup(name=PROJECT_NAME,
      version=VERSISON,
      description=DESCRIPTION ,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      intall_requires = get_requirements_list()
     )