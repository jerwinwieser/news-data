from django.shortcuts import render

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required

# for file storage
from django.core.files.storage import FileSystemStorage

# file upload
import csv
from django.contrib import messages

# get datetime
from datetime import datetime

# to read filenames
import os


@login_required(login_url='login')
def index(request):
	return render(request, 'posts/index.html', {'title': 'hi'})

@login_required(login_url='login')
def upload(request):
	if request.method == "POST":
		# get user and uploaded file
		user = request.user.get_username()
		file = request.FILES['upload_data']

		# create some var datetime
		now = datetime.now()
		date = now.strftime("%Y-%m-%d")
		time = now.strftime("%H:%M:%S")
		dt = date + '_' + time

		# create a file name to name the datafile
		fname = user + '_' + file.name
		
		# check whether the uploaded file are as expected
		# if as expected, save the file in the media folder
		# add some user feedback with error- or success-messages
		if not fname.endswith('.csv'):
			messages.error(request, 'No file Uploaded. Upload .csv instead')
		else: 
			fs = FileSystemStorage()
			fs.save(fname, file)
			messages.success(request, 'Your file has been uploaded')
	return render(request, 'posts/upload.html')

@login_required(login_url='login')
def training(request):
	# get the current user
	user = request.user.get_username()

	# list the file names in the media dir
	# then get the files from the current user
	file_names = os.listdir('media')
	user_files = [file for file in file_names if str(user) in file]

	return render(request, 'posts/training.html', {'contents': user_files})