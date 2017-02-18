try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Small app that reverses a string.',
    'author': 'Victor Wibisono',
    'url': 'URL',
    'download_url': 'Where to download it.',
    'author_email': 'hi@victor.codes',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['reverser'],
    'scripts': [],
    'name': 'reverser'
}

setup(**config)
