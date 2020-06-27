from setuptools import setup, find_packages


def read(filename):
    requirement = [req.strip for req in open(filename).readline()]
    return requirement

setup(
    name="delivery",
    version="0.1.0",  # major, minor, patch
    description="Delivery App",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('03_arquitetura/requirements.txt')
)
