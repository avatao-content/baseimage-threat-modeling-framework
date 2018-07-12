from os.path import dirname, realpath, join

from setuptools import setup, find_packages

here = dirname(realpath(__file__))

with open(join(here, 'requirements.txt'), 'r') as ifile:
    requirements = ifile.read().splitlines()

setup(
    name = 'tmf',
    version = "1.0",
    description = 'Avatao Threat Modeling Framework',
    url = '',
    author = 'Avatao.com Innovative Learning Kft.',
    author_email = 'support@avatao.com',
    license = 'custom',
    packages = find_packages('lib'),
    package_dir = {'': 'lib'},
    install_requires = requirements,
    extras_require = {
        'docs': [
            'sphinx >= 1.7.0',
        ],
    },
    zip_safe = False,
)
