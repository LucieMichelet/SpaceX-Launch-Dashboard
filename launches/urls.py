from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('launches/', views.launch_list, name='launch_list'),
    path('launches/<int:launch_id>/', views.launch_detail, name='launch_detail'),
]