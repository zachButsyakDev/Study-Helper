from django.shortcuts import render

# Create your views here.
def note_view(request):
    return render(request, "note_view.html", {})

def edit_note(request):
    return render(request, "edit_note.html", {})