"""
    作者:北辰
    日期:14-05-2019
    功能:发行版本必须的setup.py文件,包含想要发布的包的元数据
"""

# from distutils.core import setup
import setuptools

with open('README.rst') as file:
    readme = file.read()

setuptools.setup(
    # name = 'test_willie',
    name = 'testpkg_private',
    # version = '2.0.2',
    version = '2.0.0',
    packages = ['wargame'],
    # 以上是必须的字段,以下是可选的
    # url = 'https://testpypi.python.org/pypi/test_willie/',
    url = 'http://localhost:8081/simple',
    license = 'LICENSE.txt',
    # description = 'my fantasy game',
    description = 'test pkg private',
    long_description = readme,
    author = 'DMWillie',
    author_email = '2312472575@qq.com'
)