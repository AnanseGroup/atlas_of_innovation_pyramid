from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .models.meta import DBSession, Base


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.include('.models')

    # The static configuration isn't quite DRY, because all of the static assets assume that other static assets are served at /static/, as specified here.
    config.add_static_view('static', 'static', cache_max_age=3600) 
    
    # None of these pages require access to the database
    config.add_route('home', '/')
    config.add_route('map', '/map')
    config.add_route('about', '/about')
    config.add_route('goals', '/about/goals')
    config.add_route('userDocs', '/docs')
    config.add_route('devDocs', '/docs/developer')
    config.add_route('wiki', '/wiki')
    config.add_route('contribute', '/contribute')

    # individual spaces
    config.add_route('spacepage', '/wikipage/{id}')
    config.add_route('editspace', '/editspace/{id}')
    config.add_route('getspace', '/api/getSpace/{id}')
    config.add_route('change_space', '/api/changeSpace/{id}')

    # bulk actions
    config.add_route('all_innovation_spaces', '/api/getAllSpaces')
    config.add_route('singlefilterlist', '/uifunc/wikilist/{param}/{value}')
    config.add_route('singlefilter', '/searchapi/findSpacesByType')

    #     #   map.connect('/map', controller="uifunc", action="index")
    config.scan()
    return config.make_wsgi_app()
