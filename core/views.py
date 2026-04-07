from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
# Create your views here.


def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})



def course(request):
    if request.method == 'POST':
        data = request.POST
        
        course_id = data.get('course_id')
        course_name = data.get('course_name')

        Course.objects.create(
            id=course_id,
            name=course_name,
        )
        return redirect('/')

    queryset = Course.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'courses': queryset}
    return render(request, 'courses_view.html', context)

def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        data = request.POST
        course_name = data.get('course_name')

        course.name = course_name
        course.save()
        return redirect('/')

    context = {'course': course}
    return render(request, 'edit_course.html', context)


