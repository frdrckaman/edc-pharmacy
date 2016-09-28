import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'READ.md')) as readme:
     README = readme.read()

#allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
	name='edc_pharma',
	packages=find_packages(),
	include_package_data=True,
	url='https://github.com/botswana-harvard/edc-pharma.git',
	license='GPL license, see LICENSE',
	description='edc edc-pharma',
	long_description=README,
	zip_safe=False,
	keywords='edc edc-pharma',
	classifiers=[
		'Environment :: Web Environment',
        	'Framework :: Django',
        	'Intended Audience :: Developers',
        	'License :: OSI Approved :: GNU General Public License (GPL)',
        	'Operating System :: OS Independent',
        	'Programming Language :: Python',
        	# 'Programming Language :: Python :: 3',
        	# 'Programming Language :: Python :: 3.2',
        	  'Programming Language :: Python :: 3.5',
        	  'Topic :: Internet :: WWW/HTTP',
        	  'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
