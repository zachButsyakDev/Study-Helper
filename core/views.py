from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from note_page.models import Note


def welcome(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, "welcome.html")


@login_required
def home(request):
    # For now, get all notes
    # Later you can filter notes by logged-in user when your model supports it
    notes = Note.objects.all()

    return render(request, "home.html", {
        "notes": notes
    })


@login_required
def account(request):
    return render(request, "account.html")