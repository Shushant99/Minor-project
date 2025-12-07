from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
from .encoding_utils import create_and_save_encoding
from .encoding_utils import create_encodings_for_student
from django.urls import reverse
@login_required
def student_list(request):
    students = Student.objects.select_related('classroom').all()
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            create_encodings_for_student(student)
            return redirect('students:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})
@login_required
def student_list(request):
    students = Student.objects.select_related('classroom').all()
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            create_encodings_for_student(student)
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})
@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        # actually delete
        student.delete()
        return redirect('students:student_list')

    # show confirmation page
    return render(request, 'students/student_confirm_delete.html', {'student': student})
