try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This app calculates parking costs.',
    'author': 'Victor Wibisono',
    'url': 'URL',
    'download_url': 'Where to download it.',
    'author_email': 'hi@victor.codes',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['parking'],
    'scripts': [],
    'name': 'parking-calculator'
}

setup(**config)
