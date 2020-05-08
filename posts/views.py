from django.shortcuts import render

# load some libraries to set permissions
from django.contrib.auth.decorators import login_required, permission_required

# for file storage
from django.core.files.storage import FileSystemStorage

# file upload
import csv, io
from django.contrib import messages

@login_required(login_url='login')
def index(request):
	contents = {
		'title': 'hi'
	}
	return render(request, 'posts/index.html', contents)

def upload(request):
	if request.method == "POST":
		uploaded_file = request.FILES['upload_data']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)
	return render(request, 'posts/upload.html')

def uploadcsv(request):
	if request.method == "POST":
		uploaded_file = request.FILES['upload_data']
		if not uploaded_file.name.endswith('.csv'):
			messages.error(request, 'Upload your file as .csv')
		else: 
			fs = FileSystemStorage()
			fs.save(uploaded_file.name, uploaded_file)
			messages.error(request, 'Your file has been uploaded')
	return render(request, 'posts/upload.html')



# Create your views here.
# # one parameter named request
# def profile_upload(request):
#     # declaring template
#     template = "profile_upload.html"
#     data = Profile.objects.all()
# 	# prompt is a context variable that can have different values      depending on their context
#     prompt = {
#         'order': 'Order of the CSV should be name, email, address,    phone, profile',
#         'profiles': data    
#               }
#     # GET request returns the value of the data with the specified key.
#     if request.method == "GET":
#         return render(request, template, prompt)
#     csv_file = request.FILES['file']
#     # let's check if it is a csv file
#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'THIS IS NOT A CSV FILE')
#     data_set = csv_file.read().decode('UTF-8')
#     # setup a stream which is when we loop through each line we are able to handle a data in a stream
# 	io_string = io.StringIO(data_set)
# 	next(io_string)
# 	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
# 	    _, created = Profile.objects.update_or_create(
# 	        name=column[0],
# 	        email=column[1],
# 	        address=column[2],
# 	        phone=column[3],
# 	        profile=column[4]
# 	    )
# 	context = {}
# 	return render(request, template, context)