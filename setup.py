import os
from setuptools import find_packages, setup


def wd():
    return os.path.dirname(os.path.realpath(__file__))


def readme():
    path = 'README.md'
    with open(path, 'r') as f:
        return f.read()


def version():
    return '0.1.0'


setup(
    name='osri',
    version=version(),
    description='A CLI that shows parsed data from an linux os release file, usually located at /etc/os-release',
    long_description=readme(),
    url='https://github.com/odra/osri',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    license='MIT',
    maintainer='odra',
    maintainer_email='me@lrossetti.com',
    platforms=['GNU/Linux'],
    keywords=['os-release'],
    package_dir={'osri': 'src/osri'},
    zip_safe=False,
    install_requires=[
        'click==8.1.3',
        'prettytable ==3.7.0'
    ],
    tests_require=[        
        'mypy==1.1.1',
        'pytest==7.2.2',
        'pytest-sugar==0.9.6',
        'pytest-mock==3.10.0'
    ],
    entry_points={
        'console_scripts': ['osri=distri.cli:run'],
    },
)
