from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:client_id>/', views.client, name='client'),
    path('<int:license_id>/results/', views.license, name='license'),

]