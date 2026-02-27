from django.urls import path
from . import views


urlpatterns = [
    path('noteview/', views.note_view, name='note_view'),
    path('editnote/', views.edit_note, name='edit_note')
]
