import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="random-sentence-url-python",
    version="0.0.1",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/austinjp/random-sentence-url-python",
    author="austinjp",
    author_email="austin.plunkett+pypi@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8"
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={},
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=[ _ for _ in open("requirements.txt").read().split("\n") if _ ],
    python_requires="~=3.6"
)
