import json

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.attributes import flag_modified

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


@view_config(route_name='change_space', renderer='../templates/static/thanks.mako')
def changeSpace(request):
    #TO DO: implement change space for verified space
    space = request.dbsession.query(Innovation_Space).filter(Innovation_Space.primary_id==request.matchdict['id']).one()
    other_attrs = getattr(space, 'other')
    for attr, value in request.params.dict_of_lists().items():
        if getattr(space, attr, None):
            setattr(space, attr, value[-1])
        else:
            other_attrs[attr] = value
    space.other = other_attrs
    flag_modified(space, "other")
    return {'primary_id':id}  


