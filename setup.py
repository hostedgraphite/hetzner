#!/usr/bin/env python3
from distutils.core import setup

PYTHON_MODULES = [
    'hetzner',
    'hetzner.failover',
    'hetzner.rdns',
    'hetzner.reset',
    'hetzner.robot',
    'hetzner.server',
    'hetzner.util',
    'hetzner.util.addr',
    'hetzner.util.http',
    'hetzner.util.scraping',
    'hetzner.tests',
    'hetzner.tests.test_util_addr',
]

setup(name='hetzner',
      version='1.0.0',
      description='High level access to the Hetzner robot',
      url='https://github.com/aszlig/hetzner',
      author='aszlig',
      author_email='aszlig@nix.build',
      scripts=['hetznerctl'],
      py_modules=PYTHON_MODULES,
      license='BSD')
