import json

from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/makermap.mako')
@view_config(route_name='map', renderer='../templates/makermap.mako')
def map_of_innovation(request):
    return {}


@view_config(route_name='about', renderer='../templates/about.mako')
def about(request):
    return {}


@view_config(route_name='goals', renderer='../templates/goals.mako')
def goals(request):
    return {}


@view_config(route_name='userDocs', renderer='../templates/user-documentation.mako')
def userDocs(request):
    return {}


@view_config(route_name='devDocs', renderer='../templates/developer-documentation.mako')
def devDocs(request):
    return {}


@view_config(route_name='wiki', renderer='../templates/wiki.mako')
def wiki(request):
    with open('countries.json') as json_file:    
        data = json.load(json_file)
        c_list=[]
        for p in data['country']:
            c_list.append(p['countryName'])
        return {'countries':c_list}
    return {}

    