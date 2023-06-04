from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', "r") as fh:
    reqs = fh.readlines()


setup(
    name="mvts_transformer",
    version="0.0.1",
    packages=["mvts_transformer"],
    url="https://github.com/bizso09/mvts_transformer/",
    project_urls={
    },
    license="MIT License",
    author="@bizso09",
    author_email="",
    description="MVTS Transformer",
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=reqs,
)
