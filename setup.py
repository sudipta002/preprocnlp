from setuptools import setup, find_packages


setup(
    name='preprocnlp',
    version='0.1',
    license='MIT',
    author="Sudipta Ghosh",
    author_email='sudipta002@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='Pre-processing, NLP,',
    install_requires=[
          'nltk',
      ],

)