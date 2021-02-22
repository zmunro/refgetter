import setuptools

setuptools.setup(
    name="refgetter",
    version="0.0.1",
    author="Zach Munro",
    entry_points={
        "console_scripts": [
            "refgetter = refgetter:main",
        ],
    },
    install_requires=["fire", "requests", "backoff"],
    author_email="zacharymunro2@gmail.com",
    description="A refget package for retrieving data about genomic references.",
    long_description_content_type="text/markdown",
    url="https://github.com/zmunro/refgetter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
