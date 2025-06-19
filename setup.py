"""
Setup configuration for Adaptive Card Builder.
"""

from setuptools import setup, find_packages
import os


# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


setup(
    name="adaptive-card-builder",
    version="0.1.0",
    description="A Python helper library for generating Adaptive Card JSON components",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    author="Adaptive Card Builder",
    author_email="",
    url="https://github.com/yourusername/adaptive-card-builder",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies
    ],
    include_package_data=True,
    zip_safe=False,
    keywords="adaptive-cards json microsoft-teams bot-framework",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/adaptive-card-builder/issues",
        "Source": "https://github.com/yourusername/adaptive-card-builder",
        "Documentation": "https://github.com/yourusername/adaptive-card-builder#readme",
    },
)
