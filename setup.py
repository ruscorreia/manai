# setup.py
from setuptools import setup, find_packages

setup(
    name="manai",
    version="2.0.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "manai=manai.core:main",
        ],
    },
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Rosco Edutec",
    author_email="rusacorreia@hotmail.com",
    description="Assistente de Terminal Linux com IA",
    long_description=open("../README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ruscorreia/manai", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)