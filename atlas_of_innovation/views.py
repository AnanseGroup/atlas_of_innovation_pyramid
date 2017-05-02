from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.mako')
def my_view(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='map', renderer='templates/makermap.mako')
def map_of_innovation(request):
    return {'project': 'atlas-of-innovation'}
