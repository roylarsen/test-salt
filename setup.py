from setuptools import setup, find_packages

setup(
  name='test-salt',
  version='0.1',
  description="Utility for automating Vagrant and testinfra tests",
  author="Roy Larsen",
  author_email="nonades@gmail.com",
  packages=find_packages(),
  install_requires=[
    'Click',
    'testinfra',
    'python-vagrant',
  ],
  entry_points='''
    [console_scripts]
    test-salt=test_salt.cli:run
  ''',
)
