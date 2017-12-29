import json

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models.innovation_space import Innovation_Space


@view_config(route_name='singlefilterlist', renderer='../templates/list.mako')
def singlefilterpreprocess(request):
    return {'filtertype':request.matchdict['param'], 'filterparam':request.matchdict['value']}


@view_config(route_name='editspace', renderer='../templates/formedit.mako')
@view_config(route_name='getspace', renderer='json')
def getspace(request):
    space = request.dbsession.query(Innovation_Space).get(request.matchdict['id'])
    space = space.__json__(request)
    return space


@view_config(route_name='spacepage', renderer='../templates/wikipage.mako')
def getformattedspace(request):
    space = request.dbsession.query(Innovation_Space).get(request.matchdict['id'])
    space = space.__json__(request)
    formats = ["name", "primary_website", "status", "types", "description", "email",
                "street_address", "country", "twitter", "googleplus", "fablabs_url", 
                "facebook", "primary_id", "image_url", "last_updated", "latitude", 
                "longitude", "city", "state"]
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
    spaceslist = []
    for space in spaces:
        spaceslist.append(space.__json__(request="dummy request"))
    return spaceslist


@view_config(route_name='change_space', renderer='../templates/thanks.mako')
def changeSpace(request):
    #change a space
    #TO DO: implement change space for verified space

    result = request.dbsession.query(Innovation_Space).filter(Innovation_Space.primary_id==request.matchdict['id']).update(request.params)
    return {'primary_id':id}  


db_err_msg = """\
We are having some trouble fetching the data that you just requested. The failure has been logged, but if you send an email to 
"""

