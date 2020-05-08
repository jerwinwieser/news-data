from django.shortcuts import render

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required

# for file storage
from django.core.files.storage import FileSystemStorage

# file upload
import csv, io
from django.contrib import messages

# get datetime
from datetime import datetime


@login_required(login_url='login')
def index(request):
	contents = {
		'title': 'hi'
	}
	return render(request, 'posts/index.html', contents)

@login_required(login_url='login')
def upload(request):
	if request.method == "POST":
		current_user = request.user
		uploaded_file = request.FILES['upload_data']

		now = datetime.now()
		current_date = now.strftime("%Y-%m-%d")
		current_time = now.strftime("%H:%M:%S")
		current_datetime = current_date + '_' + current_time

		# create a file name to name the datafile
		write_file_name = str(current_user) + '_' + uploaded_file.name
		
		if not uploaded_file.name.endswith('.csv'):
			messages.error(request, 'Upload your file as .csv')
		else: 
			fs = FileSystemStorage()
			fs.save(write_file_name, uploaded_file)
			messages.error(request, 'Your file has been uploaded')
	return render(request, 'posts/upload.html')


