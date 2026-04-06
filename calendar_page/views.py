from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CalendarEvent


@login_required
def calendar_view(request):
    events = CalendarEvent.objects.all()

    return render(request, "calendar_view.html", {
        "events": events
    })