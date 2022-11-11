from setuptools import find_packages, setup
import sys

if sys.version_info < (3, 10):
    sys.exit('Sorry, Python < 3.10 is not supported')

setup(
    name='simple-dvr',
    version='0.0.1',
    packages=find_packages(),
    python_requires='>=3.10',
    include_package_data=True,
    license='Properitary unless otherwise stated',
    long_description=open('README.md').read(),
    install_requires=[
        'APScheduler>=3.9.1',
        'Flask>=2.2.2',
        'Jinja2>=2.11.2',
        'click>=8.1.3',
        'defusedxml>=0.7.1',
        'eventlet>=0.33.1',
        'ffmpeg>=1.4',
        'flake8>=3.8.4',
        'psutil>=5.9.2',
        'pytest>=6.2.1',
        'requests>=2.25.1'
    ],
    entry_points={
        'console_scripts': [
            'recorder = simple_dvr.recorder:cli',
        ],
    },
)
