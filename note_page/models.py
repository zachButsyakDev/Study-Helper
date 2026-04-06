from django.db import models


class NoteSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(NoteSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Untitled Note")
    content = models.TextField(blank=True)
    transcription_text = models.TextField(blank=True)

    def __str__(self):
        return self.title