# from django.conf.urls import url
from django.urls import re_path as url

from assignment import views

urlpatterns = [
    url(r'^assignment$',views.assignmentApi),
    url(r'^assignment/([0-9]+)$',views.assignmentApi) 
]
 