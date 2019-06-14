from setuptools import setup, find_packages

setup(
    name='demojd',
    description='Hello World demo with tree package structure.',
    author='vipervit',
    author_email='vitolg1@gmail.com',
    version='0.371',
    packages=find_packages(),
    package_data={'': ['*.json']},
    scripts=['demojd/scripts/hello.py']
)
