from distutils.core import setup
from setuptools import find_packages

with open("README", "r") as f:
  long_description = f.read()

setup(name='chromiumspider',  # 包名
      version='1.0.0',  # 版本号
      description='一个自动管理ChromiumDriver版本的，基于Selenium开发的自动化测试爬虫框架。',
      long_description=long_description,
      author='Lorenzo Feng',
      author_email='lorenzo.feng@njust.edu.cn',
      url='https://github.com/7emotions/ChromiumSpider',
      install_requires=[
          'selenium>=4.20.0',
      ],
      license='Apache License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Software Development :: Libraries'
      ],
      )
