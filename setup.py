from setuptools import setup


setup(
    name='dcx_utils',
    version="0.1-alpha1",
    author='Mathias Santos de Brito',
    author_email='msbrito@uesc.br',
    description='Support library to be used with Backend frameworks to add support '
                'for DCX-UI',
    license="GNU",
    keywords="dcx",
    url="http://github.com/profmathias/cet-100",
    packages=['dcx_utils'],
    long_description='This library should be used when you want to integrate some '
                     'backend frameworks with DCX-UI with Django.',
    install_requires=['django', 'djangorestframework'],
)
