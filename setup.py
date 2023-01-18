from setuptools import setup, find_packages


setup(
    name='prenlp',
    version='0.1',
    license='MIT',
    author="Sudipta Ghosh",
    author_email='sudipta002@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'nltk',
      ],

)