import json

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models.innovation_space import Innovation_Space


@view_config(route_name='singlefilterlist', renderer='../templates/list.mako')
def singlefilterpreprocess(request):
    return {'filtertype':request.matchdict['param'], 'filterparam':request.matchdict['value']}


@view_config(route_name='spacepage', renderer='../templates/wikipage.mako')
@view_config(route_name='editspace', renderer='../templates/formedit.mako')
@view_config(route_name='getspace', renderer='json')
def getspace(request):
    space = request.dbsession.query(Innovation_Space).get(request.matchdict['id'])
    space = space.__json__(request)
    formats = ["name", "primary_website", "status", "types", "description", "email",
                "street_address", "country", "twitter", "googleplus", "fablabs_url", 
                "facebook", "primary_id", "image_url", "last_updated", "latitude", "longitude"]
    formatted = {key:space[key] for key in formats} #TODO define formats
    generic = {key:space[key] for key in space if not key in formatted}
    formatted['generic'] = generic
    return formatted


@view_config(route_name='singlefilter', renderer='json')
def singlefilter(request):
    try:
        spaces = request.dbsession.query(Innovation_Space)\
            .filter(getattr(Innovation_Space, request.params['type'])==request.params['name']).all()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return translate_to_jsonable(spaces)


@view_config(route_name='all_innovation_spaces', renderer='json')
def all_innovation_spaces(request):
    try:
        spaces = request.dbsession.query(Innovation_Space).all()
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


@view_config(route_name='change_space', renderer='../templates/thanks.mako')
def changeSpace(request):
    #change a space
    #TO DO: implement change space for verified space

    print (request.params)
    result = request.dbsession.query(Innovation_Space).filter(Innovation_Space.primary_id==request.matchdict['id']).update(request.params)
    return {'primary_id':id}  


db_err_msg = """\
We are having some trouble fetching the data that you just requested. The failure has been logged, but if you send an email to 
"""

