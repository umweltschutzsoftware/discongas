from setuptools import setup, find_packages

setup(
  name='discongas',
  version='1.1.0',
  description='Implementation of VDI 3781 Part 4 to compute the discharge conditions for exhaust gases of small and medium combustion systems and other installations.',
  author='Ingenieurbüro Richters & Hüls',
  author_email='info@richtershuels.de',
  packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
  install_requires=['pandas'],
  setup_requires=['pytest-runner'],
  tests_require=['pytest==4.4.1'],
  test_suite='tests',
)
