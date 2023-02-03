from django.urls import path
from . import views

app_name = 'licenses'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:client_id>/', views.client, name='client'),
    path('<int:license_id>/results/', views.license, name='license'),
    path('detail/<int:license_id>/', views.detail, name='detail'),

]