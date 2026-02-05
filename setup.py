from setuptools import find_packages,setup

with open ("README.md","r" ,encoding="utf-8") as f:
    long_description=f.read()

__version__ = "0.0.0"

REPO_NAME = "End_To_End_LiveSensor_machine_Learning_project"
SRC_REPO = "liveSensor"
AUTHOR_USER_NAME = "peetlasriram"
AUTHOR_EMAIL = "peetlasriram40@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,

    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "liveSensor"},
    packages=find_packages(where="liveSensor")
)