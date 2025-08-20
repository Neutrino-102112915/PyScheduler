from setuptools import setup, find_packages

setup(
    name="PyScheduler",
    version="0.1.0",
    author="Neutrino-102112915",
    description="A simple Python auto scheduler for tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Neutrino-122112915/PyScheduler",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        # Add dependencies if any
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
