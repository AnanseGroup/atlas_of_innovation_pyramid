import json

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models.innovation_space import Innovation_Space



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


db_err_msg = """\
We are having some trouble fetching the data that you just requested. The failure has been logged, but if you send an email to 
"""

