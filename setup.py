import setuptools

setuptools.setup(
    name="matplotlibHistos",
    version="0.0.1",
    author="Kurt Brendlinger",
    author_email="kurt.brendlinger@gmail.com",
    description="A package with histogramming tools",
    url="https://github.com/brendlin/matplotlibHistos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy>=0.11",
                      "matplotlib",
                      ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
