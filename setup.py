import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ucsd_algorithms_course1", # Replace with your own username
    version="0.0.1",
    author="Tobias",
    author_email="tobias.datascience@gmail.com",
    description="Collection of modules for the UCSD course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaabberwocky/ucsd-algorithms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)