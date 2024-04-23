from django.urls import path
from . import views

urlpatterns = [
    path('postcontact/', views.post_contact_api_views, name='postcontact'),
    path('getcontact/', views.get_contact_api_views, name='getcontact')
]