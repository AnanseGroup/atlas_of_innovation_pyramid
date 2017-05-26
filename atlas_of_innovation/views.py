import json

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models.innovation_space import Innovation_Space


@view_config(route_name='boilerplate', renderer='templates/mytemplate.mako')
def my_view(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='home', renderer='templates/makermap.mako')
@view_config(route_name='map', renderer='templates/makermap.mako')
def map_of_innovation(request):
    return {}

@view_config(route_name='about', renderer='templates/about.mako')
def about(request):
    return {}

@view_config(route_name='goals', renderer='templates/goals.mako')
def goals(request):
    return {}

@view_config(route_name='userDocs', renderer='templates/user-documentation.mako')
def userDocs(request):
    return {}

@view_config(route_name='devDocs', renderer='templates/developer-documentation.mako')
def devDocs(request):
    return {}

@view_config(route_name='wiki', renderer='templates/wiki.mako')
def wiki(request):
    with open('countries.json') as json_file:    
        data = json.load(json_file)
        print (data)
        c_list=[]
        for p in data['country']:
            c_list.append((p['countryName']))
        return {'countries':c_list}
    return {}


@view_config(route_name='all_innovation_spaces', renderer='json')
def all_innovation_spaces(request):
    try:
        spaces = request.dbsession.query(Innovation_Space).all()
        print(spaces)
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return translate_to_jsonable(spaces)

def translate_to_jsonable(spaces):
    columns = [x.__str__().split('.')[1] for x in Innovation_Space.__table__.columns]
    spaceslist = []
    for space in spaces:
        spaceslist.append({ column: getattr(space, column) for column in columns })
    return spaceslist


@view_config(route_name='filter_innovation_spaces', renderer='json')
def filter_innovation_spaces(request):
    return {'project': 'atlas-of-innovation'}   


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_tutorial_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

