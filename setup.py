import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="addition_example",
    version="0.0.1",
    author="Jonathan",
    description="Simple example of a package for adding numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonathan-marsan/addition_example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
