"""Bars API Install Script."""
import os
from setuptools import setup, find_packages

TOPDIR = os.path.dirname(__file__) or "."

requires = [
    'click',
    'Flask',
    'loguru',
    'requests',
    'waitress']
with open(TOPDIR + '/README.md', 'r') as f:
    readme = f.read()
about = {}
with open(TOPDIR + '/turn_bot/__version__.py', 'r') as f:
    exec(f.read(), about)
setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/x-rst',
    author=about['__author__'],
    url=about['__url__'],
    author_email=about['__author_email__'],
    license=about['__license__'],
    packages=find_packages(),
    python_requires=">=3.5",
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=requires,
    include_package_data=True,
    entry_points='''
        [console_scripts]
        turn_bot=turn_bot.cli:prod_server
        turn_bot_dev=turn_bot.cli:dev_server
    ''',
    dependency_links=[],
    zip_safe=False
)
