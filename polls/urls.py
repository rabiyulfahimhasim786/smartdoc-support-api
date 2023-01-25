from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdf/', views.UserList.as_view()),
    path('pdf/<int:pk>/', views.Userupdate.as_view()),
    path('pdfurl/', views.pdfurl, name='pdfurl'),
    path('output/', views.OutputList.as_view()),
    path('output/<int:pk>/', views.Outputupdate.as_view()),
]