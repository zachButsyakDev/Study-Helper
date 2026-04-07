from django.shortcuts import render, redirect, get_object_or_404
from .models import CalendarEvent, 

# Create your views here.
def calendar(request):
    return render(request, "calendar_view.html", {})

def update_calendar_event(request, id):
    event = get_object_or_404(CalendarEvent, id=id)
    if request.method == 'POST':
        data = request.POST
        event_name = data.get('event_name')
        event_date = data.get('event_date')

        event.name = event_name
        event.date = event_date
        event.save()
        return redirect('/')

    context = {'event': event}
    return render(request, 'edit_calendar_event.html', context)

def delete_calendar_event(request, id):
    event = get_object_or_404(CalendarEvent, id=id)
    event.delete()
    return redirect('/')

def create_calendar_event(request):
    if request.method == 'POST':
        data = request.POST
        event_name = data.get('event_name')
        event_date = data.get('event_date')

        CalendarEvent.objects.create(
            name=event_name,
            date=event_date,
        )
        return redirect('/')

    return render(request, 'create_calendar_event.html', {})

def notifications(request):
    return render(request, "notifications_view.html", {})


def mark_notification_as_read(request, id):
    notification = get_object_or_404(Notification, id=id)
    notification.mark_as_read()
    return redirect('/notifications')

def delete_notification(request, id):
    notification = get_object_or_404(Notification, id=id)
    notification.delete()
    return redirect('/notifications')

def create_notification(request):
    if request.method == 'POST':
        data = request.POST
        event_id = data.get('event_id')
        message = data.get('message')

        event = get_object_or_404(CalendarEvent, id=event_id)

        Notification.objects.create(
            user_id=request.user,
            event_id=event,
            message=message,
        )
        return redirect('/notifications')

    return render(request, 'create_notification.html', {})