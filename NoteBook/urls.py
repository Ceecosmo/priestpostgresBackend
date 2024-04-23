from django.urls import path
from . import views

urlpatterns = [
    path('postNoteBook/', views.post_NoteBook_api_views, name='postNoteBook'),
    path('getNoteBook/', views.get_NoteBook_api_views, name='geNoteBook')
]