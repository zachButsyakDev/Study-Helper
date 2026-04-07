# from django.shortcuts import render

# # Create your views here.
# def note_view(request):
#     return render(request, "note_view.html", {})

# def edit_note(request):
#     return render(request, "edit_note.html", {})

from django.shortcuts import render, redirect, get_object_or_404
from .models import NoteSection, Note


def noteSection(request):
    if request.method == 'POST':
        data = request.POST
        
        section_id = data.get('section_id')
        note_section_name = data.get('note_section_name')

        NoteSection.objects.create(
            section_id=section_id,
            name=note_section_name,
        )
        return redirect('/')

    queryset = NoteSection.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'notes': queryset}
    return render(request, 'notes_view.html', context)


def delete_note_section(request, id):
    note = get_object_or_404(NoteSection, id=id)
    note.delete()
    return redirect('/')


def update_note_section(request, id):
    note = get_object_or_404(NoteSection, id=id)
    if request.method == 'POST':
        data = request.POST
        note_section_name = data.get('note_section_name')

        note.name = note_section_name
        note.save()
        return redirect('/')

    context = {'note': note}
    return render(request, 'edit_note.html', context)


def note(request):
    if request.method == 'POST':
        data = request.POST
        note_id = data.get('note_id')
        note_section_id = data.get('note_section_id')
        content = data.get('content')
        transcription = data.get('transcription')
        
        Note.objects.create(
            note_id=note_id,
            section_id_id=note_section_id,
            content=content,
            transcription=transcription
        )
        return redirect('/')
    
    queryset = Note.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(content__icontains=request.GET.get('search'))

    context = {'notes': queryset}
    return render(request, 'notes.html', context)


def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('/')


def update_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        data = request.POST
        note_section_id = data.get('note_section_id')
        content = data.get('content')
        transcription = data.get('transcription')

        note.section_id_id = note_section_id
        note.content = content
        note.transcription = transcription
        note.save()
        return redirect('/')

    context = {'note': note}
    return render(request, 'update_note.html', context)