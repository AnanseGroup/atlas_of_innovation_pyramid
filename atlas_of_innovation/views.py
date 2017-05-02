from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.mako')
def my_view(request):
    return {'project': 'atlas-of-innovation'}

@view_config(route_name='map', renderer='templates/makermap.mako')
def map_of_innovation(request):
    return {'project': 'atlas-of-innovation'}

# @view_config(route_name='about', renderer='templates/about.mako')
# def map_of_innovation(request):
#     return {'project': 'atlas-of-innovation'}

# @view_config(route_name='goals', renderer='templates/goals.mako')
# def map_of_innovation(request):
#     return {'project': 'atlas-of-innovation'}

# @view_config(route_name='userDocs', renderer='templates/user-documentation.mako')
# def map_of_innovation(request):
#     return {'project': 'atlas-of-innovation'}

# @view_config(route_name='devDocs', renderer='templates/developer-documentation.mako')
# def map_of_innovation(request):
#     return {'project': 'atlas-of-innovation'}

		
    
    # def goals(self):
    #     return render('/goals.html')

    # def userDocs(self):
    # 	return render('/user-documentation.html')

    # def devDocs(self):
    # 	return render('/developer-documentation.html')