from setuptools import setup, find_packages
setup(
    name = "extraction",
    version = "0.1",
    packages = find_packages(),

    namespace_packages = ["londonriots"],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ["londonriots.feeds"]

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt", "*.rst"],
    },

    # metadata for upload to PyPI
    author = "Evan Cofsky",
    author_email = "evan@tunixman.com",
    description = "Feature Extractor for The London Riots.",
    license = "GPLv3",
    url = "https://github.com/tunixman/The-London-Riots",
)
