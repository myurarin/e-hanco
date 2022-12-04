from setuptools import setup
from setuptools import find_packages

setup(name='e-hanco',
      version='0.0.1',
      description='日付入りのハンコ作成ソフト',
      author='YuyaMatsuura',
      author_email='',
      url='',
      packages=find_packages("e-hanco"),
      install_requires=[
          "Pillow"
      ]
      )
