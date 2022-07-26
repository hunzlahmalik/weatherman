import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='weatherman',
    version='0.0.1',
    description='Weatherman for training',
    py_modules=['weatherman'],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        'console_scripts': [ 
            'weatherman = weatherman.__main__:main',
        ]
    } ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/crackaf/weatherman",
    author="Hunzlah Malik",
    author_email="hunzlahmalik@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
    ],
    extras_require={
        "test": [
            "pytest>=7.1.2",
        ]
    }
)