from setuptools import find_packages, setup
setup(
    name='uol_common',
    packages=find_packages(include=['polar_distance']),
    version='0.1.0',
    description='UOL Common Library Functions',
    author='Steven Perez',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)



# from setuptools import setup
# setup(name='litfibreCommon',
# version='0.2.2',
# description= 'Functions for litfibre server management',
# url='#',
# author= 'Steven Perez',
# author_email= 'steven.perez@litfibre.com',
# packages=["logger","v2_lutils","lutils","v2_lsecrets","lsecrets","v2_alerts","alerts"],
# zip_safe= False)