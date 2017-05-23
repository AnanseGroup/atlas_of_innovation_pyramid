from pyramid.view import view_config


@view_config(route_name='boilerplate', renderer='templates/mytemplate.mako')
def my_view(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='home', renderer='templates/makermap.mako')
@view_config(route_name='map', renderer='templates/makermap.mako')
def map_of_innovation(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='about', renderer='templates/about.mako')
def about(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='goals', renderer='templates/goals.mako')
def goals(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='userDocs', renderer='templates/user-documentation.mako')
def userDocs(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='devDocs', renderer='templates/developer-documentation.mako')
def devDocs(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='wiki', renderer='templates/wiki.mako')
def wiki(request):
    return {'project': 'atlas-of-innovation'}

