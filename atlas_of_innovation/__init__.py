from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('map', '/')
    config.add_route('about', '/about')
    config.add_route('goals', '/about/goals')
    config.add_route('userDocs', '/docs')
    config.add_route('devDocs', '/docs/developer')
    config.add_route('home', '/old_home')

    #     #   map.connect('/map', controller="uifunc", action="index")
    config.scan()
    return config.make_wsgi_app()
