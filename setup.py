from setuptools import setup, find_packages

setup(
    name = 'portality',
    version = '0.8.0',
    packages = find_packages(),
    install_requires = [
        "Flask==0.8",
        "Flask-Login",
        "Flask-WTF",
        "requests==1.1.0",
        "markdown",
        "gitpython"
        #"lxml"
    ],
    url = 'http://cottagelabs.com/',
    author = 'Cottage Labs',
    author_email = 'us@cottagelabs.com',
    description = 'A web API layer over an ES backend, with various useful views',
    license = 'Copyheart',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
