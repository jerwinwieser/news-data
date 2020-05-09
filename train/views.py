from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import numpy as np
import os
from django.contrib.auth import get_user_model


User = get_user_model()

def render_chart(request, *args, **kwargs):
	return render(request, 'train/chart.html')

class rest_data(APIView):
	authentication_classes = []
	permission_classes = []
	def get(self, request, format=None):
		qs_count = User.objects.all().count()

		labels = ["Users", "Blue", "Yellow"]
		default_items = [qs_count, 7, 9]
		data = {
				'labels': labels,
				'default': default_items,
		}
		return Response(data)

def api_data(request, *args, **kwargs):
	data = {
		'sales': 100,
		'customers': 10,
	}
	return JsonResponse(data)