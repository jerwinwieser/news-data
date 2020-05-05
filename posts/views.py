from django.shortcuts import render

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required

# for file storage
from django.core.files.storage import FileSystemStorage

@login_required(login_url='login')
def index(request):
	contents = {
		'title': 'hi'
	}
	return render(request, 'posts/index.html', contents)

def upload(request):
	if request.method == "POST":
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)
	return render(request, 'posts/upload.html')