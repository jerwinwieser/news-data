from django.shortcuts import render

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required

# for file storage
from django.core.files.storage import FileSystemStorage

# file upload
import pandas as pd
import numpy as np
from django.contrib import messages

# get datetime
from datetime import datetime

# to read filenames
import os

# handle data for charts
from django.http import JsonResponse

def graph(request, *args, **kwargs):
	return render(request, 'posts/charts.html', {})

def get_data(request, *args, **kwargs):
	data = {
		'sales': 100,
		'customers': 10,
	}
	return JsonResponse(data)

@login_required(login_url='login')
def index(request):
	return render(request, 'posts/index.html', {'title': 'hi'})

@login_required(login_url='login')
def upload(request):
	# get user and uploaded file
	# create some var datetime
	# create a file name to name the datafile
	# check whether the uploaded file are as expected
	# if as expected, save the file in the media folder
	# add some user feedback with error- or success-messages
	if request.method == "POST":
		user = request.user.get_username()
		file = request.FILES['upload_data']

		now = datetime.now()
		date = now.strftime("%Y-%m-%d")
		time = now.strftime("%H:%M:%S")
		dt = date + '_' + time

		fname = user + '_' + file.name

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
	# list the file names in the media dir
	# then get the files from the current user
	# read in the data file
	# convert to numpy array
	# create context to render
	user = request.user.get_username()

	file_names = os.listdir('media')
	user_files = [file for file in file_names if str(user) in file]

	df = pd.read_csv('media/' + user_files[1])
	x = np.array(df.PassengerId)

	context = {
		'filenames': user_files[1],
		'dataframes': x,
	}
	return render(request, 'posts/training.html', context)