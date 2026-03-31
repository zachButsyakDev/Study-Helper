# forms.py
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['notes_title', 'notes_description', 'notes_image']