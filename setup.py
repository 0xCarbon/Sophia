from setuptools import setup, find_packages

setup(
  name = 'Sophia-Optimizer',
  packages = find_packages(exclude=[]),
  version = '0.2.1',
  license='APACHE',
  description = 'Sophia Optimizer',
  author = 'Joao Canesin',
  author_email = 'joao@0xcarbon.org',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/0xCarbon/Sophia',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'optimizers',
    "Prompt Engineering"
  ],
  install_requires=[
    'torch',
    'datasets',
    'transformers',

  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)