from django.urls import path
from . import views 

urlpatterns = [
  path('', views.home, name="home"),
  path('add/', views.add, name="add"),
  path('edit_st/<int:pk>/', views.sturec_edit, name="edit"),
  path('last-item/', views.last_item, name="lastItem"),
  path('find-item/', views.find_item, name="finditem"),
  path('heading/', views.heading, name="heading"),
]