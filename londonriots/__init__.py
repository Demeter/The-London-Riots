from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from londonriots.models import appmaker

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    get_root = appmaker(engine)
    config = Configurator(settings=settings, root_factory=get_root)
    config.add_static_view('static', 'londonriots:static')
    config.add_view('londonriots.views.view_root',
                    context='londonriots.models.MyRoot',
                    renderer="templates/root.pt")
    config.add_view('londonriots.views.view_model',
                    context='londonriots.models.MyModel',
                    renderer="templates/model.pt")
    return config.make_wsgi_app()
