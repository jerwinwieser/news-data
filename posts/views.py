from django.shortcuts import render

def index(request):
	contents = {
		'title': 'hi'
	}
	return render(request, 'posts/index.html', contents)