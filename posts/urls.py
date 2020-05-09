from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='posts-index'),
    path('upload/', views.upload, name='posts-upload'),
    path('training/', views.training, name='posts-training'),
    path('api/data/', views.get_data, name='api-data'),
 	path('graph/', views.chart_data.as_view(), name='posts-graph'),   
]
