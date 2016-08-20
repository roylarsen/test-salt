from setuptools import setup, find_packages

setup(
  name='test-salt',
  version='0.1',
  packages=find_packages(),
  install_requires=[
    'Click',
    'testinfra',
  ],
  entry_points='''
    [console_scripts]
    test-salt=test_salt.cli:run
  ''',
)
