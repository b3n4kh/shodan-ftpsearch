import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ftpsearch",
    version="0.0.1",
    author="Benjamin Akhras",
    author_email="b@akhras.at",
    description="Shodan FTP Search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/b3n4kh/ftpsearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'shodan',
        'Click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'ftpsearch=ftpsearch.cli:cli'
        ],
    },
    include_package_data=True,
    python_requires='>=3.6',
)
