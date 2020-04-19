from django.shortcuts import render
from .models import Courses
from .forms import CoursesForm


# Create your views here.


def index(request):
    courses = Courses.objects.all()
    return render(request, 'index.html', {'courses': courses})


def details(request, slug):
    courses = Courses.objects.filter(slug=slug)
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            course = Courses()
            course.name = form.cleaned_data['name']
            course.description = form.cleaned_data['message']
            course.slug = form.cleaned_data['name']
            course.save()
            return index(request)
    else:
        form = CoursesForm()

    return render(request, 'details.html', {'courses': courses, 'form': form})
