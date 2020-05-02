from django.shortcuts import render

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url='login')
def index(request):
	contents = {
		'title': 'hi'
	}
	return render(request, 'posts/index.html', contents)