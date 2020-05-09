from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='posts-index'),
    path('upload/', views.upload, name='posts-upload'),
    path('api/data/', views.api_data, name='api-data'),
 	path('api/chart/data/', views.chart_data.as_view(), name='chart-data'),
 	path('api/chart/', views.chart, name='chart'),
]