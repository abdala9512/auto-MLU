from setuptools import find_packages, setup

setup(
    name='auto-mlu',
    packages=find_packages(include=['automlu']),
    version='0.3.0',
    description='Utilities for Machine learning development',
    author='Miguel Arquez Abdala',
    license='MIT',
    install_requires=["scikit-learn"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)