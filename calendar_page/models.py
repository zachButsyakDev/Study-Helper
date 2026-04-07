from django.db import models
from django.contrib.auth.models import User
#this model stores calendar events for a user

class CalendarEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        # Delete all related notifications when a CalendarEvent is deleted
        self.notification_set.all().delete()
        super().delete(*args, **kwargs)
          
    def save(self, *args, **kwargs):
        # Ensure that the event title is not empty
        if not self.title.strip():
            raise ValueError("Event title cannot be empty.")
        super().save(*args, **kwargs)
          
    def update_title(self, new_title):
        self.title = new_title
        self.save()
          
    def get_title(self):
        return self.title


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
         
    def save(self, *args, **kwargs):
        # Ensure that the notification message is not empty
        if not self.message.strip():
            raise ValueError("Notification message cannot be empty.")
        super().save(*args, **kwargs)
    
    def mark_as_read(self):
        self.is_read = True
        self.save()