from setuptools import find_packages,setup
from typing import List

requirement_file_name = 'requirements.txt'
REMOVE_PACKAGE = '-e .'

def get_requirement()->List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readline()
    requirement_list = [requirement_file.replace("/n","") for requirement_name in requirement_list]

    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list


setup(name = "Insurance",
      version = "0.0.1",
      description = "Insurance Industry Level Project",
      author = "Bhavesh Chavan",
      author_email = "chavanbhavesh60@gmail.com",
      packages = find_packages(),
      install_requires = get_requirement())