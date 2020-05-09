from django.urls import path

from . import views


urlpatterns = [
    path('', views.render_chart, name='train-chart'),
    path('rest/', views.rest_data.as_view(), name='train-rest-data'),
]