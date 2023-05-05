
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('data/',views.file,name='data'),
    path('dataform/',views.form1,name='form1'), 
]