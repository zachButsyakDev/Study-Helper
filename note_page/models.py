from django.db import models


# this model represents courses/class section
class NoteSection(models.Model):
    section_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Delete all related notes when a NoteSection is deleted
        self.note_set.all().delete()
        super().delete(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        # Ensure that the section name is unique
        if NoteSection.objects.filter(name=self.name).exclude(section_id=self.section_id).exists():
            raise ValueError("A NoteSection with this name already exists.")
        super().save(*args, **kwargs)
        
    
    def update_name(self, new_name):
        if NoteSection.objects.filter(name=new_name).exclude(section_id=self.section_id).exists():
            raise ValueError("A NoteSection with this name already exists.")
        self.name = new_name
        self.save()
        
    def get_notes(self):
        return self.note_set.all()


# individual note
class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    section_id = models.ForeignKey(NoteSection, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    transcription_text = models.TextField(blank=True)

    def __str__(self):
        return self.content[:50]
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        # Ensure that the content is not empty
        if not self.content.strip():
            raise ValueError("Note content cannot be empty.")
        super().save(*args, **kwargs)
    
    def update_content(self, new_content):
        self.content = new_content
        self.save()
        
    def get_content(self):
        return self.content
        
    
