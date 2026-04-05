"""
Setup configuration for Information Field Theory Core Library
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ift-core",
    version="1.0.0",
    author="Juan Diego Vicente Gabancho",
    author_email="jdvg@physics.org",
    description="Information Field Theory: Unified framework for physics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JuanDiegoVG/IFT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7+",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "scipy>=1.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.10.1",
            "black>=20.8b1",
            "flake8>=3.8.4",
        ],
        "docs": [
            "sphinx>=3.0",
            "sphinx-rtd-theme>=0.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "ift-verify=ift:verify_core_predictions",
        ],
    },
)
