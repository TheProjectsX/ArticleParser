from setuptools import setup, find_packages

setup(
    name='ArticleParser',
    version='0.1',
    packages=find_packages(),
    # Description
    description='Parse Articles from WEB via Search Query',
    long_description='A Python package for parsing articles from various sources just via Search Query',
    long_description_content_type='text/markdown',
    # Author information
    author='TheProjectsX',
    author_email='',
    # Project URL
    url='https://github.com/TheProjectsX/ArticleParser',
    # License information
    license='MIT',
    # Dependencies
    install_requires=[
        'googlesearch-python==1.2.3',
        'requests==2.31.0',
        'beautifulsoup4==4.12.3',
        'newspaper3k==0.2.8',
        'wikipedia==1.4.0',
        'html2text==2024.2.26',
    ],
    # Include additional files
    include_package_data=True,
    # Additional classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
