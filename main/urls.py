from django.urls import path
from main import views
urlpatterns=[
    path('',views.home, name="home"),
    path('deleteTask/<int:i>/', views.deleteTask, name="delete")
]