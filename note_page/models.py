from django.db import models


# this model represents courses/class section
class NoteSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# individual note
class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(NoteSection, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    transcription_text = models.TextField(blank=True)

    def __str__(self):
        return self.content[:50]
