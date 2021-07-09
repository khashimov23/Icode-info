from django.shortcuts import render, redirect
from .models import *
from .forms import *

def student_list(request):
    grant_studentlar = Student.objects.filter(grant=True)
    kontrakt_studentlar = Student.objects.filter(grant=False)

    context = {
        'grant_studentlar': grant_studentlar,
        'kontrakt_studentlar': kontrakt_studentlar
    }
    return render(request, 'blog/student_list.html', context)
    

def teachers_list(request):
    teacherlar = Teacher.objects.all()

    return render(request, 'blog/teacher_list.html', {'teacherlar': teacherlar})



def xona_list(request):
    xonalar = Xona.objects.all()

    return render(request, 'blog/xona_list.html', {'xonalar': xonalar})


def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)

    return render(request, 'blog/teacher_detail.html', {'teacher': teacher})


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/icode/students/')

    else:
        form = StudentForm()

    return render(request, 'blog/student_form.html', {'form': form})