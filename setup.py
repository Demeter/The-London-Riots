from setuptools import setup, find_packages
setup(
    name = "londonriots",
    version = "0.1",
    packages = find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ["requests",
                        "feedparser",
                        "feedcache",
                        "sqlalchemy",
                        "pg8000",
                        "BeautifulSoup",
                        "nltk"
                        ],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
    },

    test_suite = "londonriots",
    test_loader = "unittest"
    # metadata for upload to PyPI
    author = "Evan Cofsky",
    author_email = "evan@tunixman.com",
    description = "The London Riots currency trading system.",
    license = "GPLv3",
    url = "https://github.com/tunixman/The-London-Riots",
)
