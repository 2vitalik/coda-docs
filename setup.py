import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coda-docs",
    version="0.3.7",
    author="Vitalik",
    author_email="2vitalik@gmail.com",
    description="Coda data for different projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/2vitalik/coda-docs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
