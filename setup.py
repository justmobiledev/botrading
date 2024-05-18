from setuptools import setup, find_packages

setup(
    name='botrading',
    version='1.0',
    packages=find_packages(),
    description='A package with utilities for algorithmic trading',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/justmobiledev/botrading',
    author='B/O Trading Blog',
    author_email='',
    license='MIT',
    install_requires=[
        'lxml==5.2.2',
        'numpy==1.26.4',
        'pandas==2.2.2',
        'pandas_market_calendars==4.4.0',
        'requests==2.31.0',
        'pytz==2024.1',
        'matplotlib==3.9.0',
        'seaborn==0.13.2',
        'alpaca-py==0.21.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',
)