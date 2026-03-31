from django.urls import path
from . import views


urlpatterns = [
    path('notesection/', views.noteSection, name='note_section'),
    path('updatenotesection/<int:id>/', 
         views.update_note_section, 
         name='update_note_section'
    ),
    path(
        'deletenotesection/<int:id>/',
        views.delete_note_section,
        name='delete_note_section'
    ),
    path('note/', views.note, name='note'),
    path('updatenote/<int:id>/', views.update_note, name='update_note'),
    path('deletenote/<int:id>/', views.delete_note, name='delete_note'),
]
