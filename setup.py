import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Py-Dictionary",
    version="1.0.1",
    author="nit-in",
    author_email="nit_in@live.com",
    description="Dictionary module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nit-in/py-dictionary",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests", "bs4", "stringcolor",],
)
