from django.urls import path 
from  interviewapp import views
urlpatterns = [
    path('',views.index, name='index'),
     path('add_emp',views.add_emp, name='add_emp'),
   
    
]
