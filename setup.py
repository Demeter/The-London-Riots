import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'sqlalchemy',
    'zope.sqlalchemy',
    'requests',
    'feedparser',
    'feedcache',
    'pg8000',
    'BeautifulSoup',
    'nltk'
    ]

if sys.version_info[:3] < (2,5,0):
    requires.append('pysqlite')

setup(name='londonriots',
      version='0.1',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author = "Evan Cofsky",
      author_email = "evan@tunixman.com",
      description = "The London Riots currency trading system.",
      license = "GPLv3",
      url = "https://github.com/tunixman/The-London-Riots",
      keywords='web pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      tests_require = requires,
      test_suite="londonriots",
      entry_points = {"paste.app_factory": ["main = londonriots:main"],
                      "console_scripts": ["pginit = londonriots.scripts.pginit:main",
                                          "load_currency_pairs = londonriots.scripts.load_currency_pairs:main",
                                          "trade_history = londonriots.scripts.trade_history:main",
                                          "article_history = londonriots.scripts.article_history:main"]},
      paster_plugins=['pyramid'],
      )

