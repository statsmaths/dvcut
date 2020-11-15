from setuptools import setup
from setuptools import find_packages

long_description= """
The Distant TV Toolkit is a Python package designed to facilitate the
computational analysis of visual culture.
"""

required = [
    "numpy",
    "pandas",
    "scipy",
    "opencv-python",
    "matplotlib",
    "progress"
]

extras = {
    "tests": [
        "pytest",
        "pytest-pep8",
        "pytest-xdist",
        "pytest-cov",
        "codecov"
    ],
    "optional": ["scikit-image"]
}

setup(
    name="dvcut",
    version="0.0.1",
    description="Detecting Cuts in Moving Images",
    long_description=long_description,
    author="Taylor Anold, Lauren Tilton",
    author_email="taylor.arnold@acm.org",
    url="https://github.com/statsmaths/dvcut",
    license="GPL-2",
    install_requires=required,
    extras_require=extras,
    classifiers=[
        "Topic :: Multimedia :: Video",
    ],
    packages=find_packages(),
)
