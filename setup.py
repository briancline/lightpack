from setuptools import setup
from lightpack.version import version_str

setup(
    name='lightpack',
    version=version_str,
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    description='Controls Lightpack devices through a common Python API',
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='lightpack api',
    url='https://github.com/briancline/lightpack',
    packages=['lightpack'],
    install_requires=open('requirements.txt').readlines(),
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Home Automation',
    ],
)
