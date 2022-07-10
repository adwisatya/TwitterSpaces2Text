from distutils.core import setup, Extension
import subprocess

try:
  subprocess.run(["pandoc","-v"])
  subprocess.run(["pandoc","--from=markdown","--to=rst","--output=README","README.md"])
except:
  pass

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'TwitterSpaces2Text',
  packages = ['TwitterSpaces2Text'],
  version = '0.1.1',
  license='MIT',
  description = 'This library helps you to download Twitter Spaces text/caption',
  long_description=long_description,
  author = 'Aryya Widigdha',
  author_email = 'aryya.widigdha@yahoo.com',
  url = 'https://github.com/adwisatya/TwitterSpaces2Text',
  download_url = 'https://github.com/adwisatya/TwitterSpaces2Text/archive/refs/tags/v0.1.tar.gz',
  keywords = ['twitter', 'spaces', 'twitter spaces text'],
  install_requires=[
          'requests',
      ],
  classifiers=[
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
