from setuptools import setup
import setuptools

read1 = open("README1.md", "r")
read2 = read1.read()
long_description = read2

setup(
    name='finance_py',
    version='0.0.1',
    description="A GUI Music Player with all the basic functions, which is developed using Tkinter",
    author='Smit.G , Aishwarya.B , Abhinav.T',
    #   url='https://github.com/Spidy20/PyMusic_Player',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['finance python', 'money', 'investment', 'balloon balance'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    py_modules=['finance_py'],
    package_dir={'': 'src'},
    install_requires=[
        'mutagen'
    ])
