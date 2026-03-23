from django.db import models

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(NoteSection, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    transcription_text = models.TextField(blank=True)

    def __str__(self):
        return self.content[:50]
