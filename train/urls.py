from django.urls import path

from . import views


urlpatterns = [
    path('', views.render_chart, name='train-chart'),
    path('rest/', views.rest_data.as_view(), name='train-rest-data'),
    path('api/', views.api_data, name='train-api-data'),
]