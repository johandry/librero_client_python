from setuptools import setup, find_packages

setup(
    name="librero_client",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Johandry Amador",
    author_email="johandry@gmail.com",
    description="A Librero client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nydasco/package_publishing",
    classifiersz=[
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: Microsoft :: Windows",
      "Intended Audience :: Education",
    ],
    python_requires='>=3.9',
)