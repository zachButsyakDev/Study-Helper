from django.db import models
# Will need to import User class for user_id

class CalendarEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title


class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
