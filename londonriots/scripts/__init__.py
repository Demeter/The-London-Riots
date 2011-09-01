"""Command-line scripts for londonriots."""

import sys
from contextlib import contextmanager
from pyramid.paster import bootstrap
import logging.config as lconf

@contextmanager
def environment(argv=sys.argv):
    """Handles initializing and closing down the app and logging."""

    ini_path = argv[1]
    env = bootstrap(ini_path)
    lconf.fileConfig(ini_path)

    try:
        yield env
    finally:
        env["closer"]()
