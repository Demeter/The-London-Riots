"""Command-line scripts for londonriots."""

import sys
from contextlib import contextmanager
from pyramid.paster import bootstrap
import logging.config as lconf
import londonriots.models as models
from paste.deploy import appconfig
from sqlalchemy import engine_from_config

@contextmanager
def environment(argv=sys.argv):
    """Handles initializing and closing down the app and logging."""

    ini_path = argv[1]
    env = bootstrap(ini_path)
    lconf.fileConfig(ini_path)

    conf = appconfig('config:' + ini_path, 
            relative_to=".")

    # Bind Engine Based on Config
    engine = engine_from_config(conf, 'sqlalchemy.')
    models.initialize_sql(engine)

    try:
        yield env
    finally:
        env["closer"]()
