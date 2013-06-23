#from distutils.core import setup
from setuptools import setup
import py2exe

setup(
    name='tellprox',
    version='0.22',
    author='Pete Cracknell',
    author_email='p3tecracknell@gmail.com',
    packages=['tellprox'],
    package_data={'tellprox': ['static/css/*.css']},
	install_requires=['cherrypy','configobj','bottle'],
	dependency_links = ['https://github.com/erijo/telldus-py.git#egg=telldus-py'],
    url='https://github.com/p3tecracknell/tellprox',
    license='LICENSE.txt',
    description='Python API to replicate Telldus Live',
    long_description=open('README.md').read(),
)