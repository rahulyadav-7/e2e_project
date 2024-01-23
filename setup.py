from setuptools import find_packages,setup
setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Rahul Yadav',
    author_email='ry7.rahulyadav@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)

