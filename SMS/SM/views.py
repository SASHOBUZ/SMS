from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Sum

from .forms import *

from .models import *

# Create your views here.()


def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    total_fees = list(Fees.objects.aggregate(
        Sum('amount')).values())[0]
    total_students = students.count()
    total_teachers = teachers.count()
    context = {'students': students, 'teachers': teachers,
               'total_students': total_students, 'total_teachers': total_teachers,
               'total_fees': total_fees}
    return render(request, 'sm/dashboard.html', context)


def Students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'sm/student_info.html', context)


def Teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'sm/teacher_info.html', context)


def Account(request):
    accounts = Fees.objects.all()
    total_fees = list(Fees.objects.aggregate(
        Sum('amount')).values())[0]
    context = {'accounts': accounts, 'total_fees': total_fees}
    return render(request, 'sm/accounts.html', context)


def CreateStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'sm/student_form.html', context)


def UpdateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'sm/student_form.html', context)


def DeleteStudent(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('/')
    context = {'item': student}
    return render(request, 'sm/delete.html', context)


def CreateTeacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'sm/teacher_form.html', context)


def UpdateTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'sm/teacher_form.html', context)


def AddFees(request):
    form = FeesForm()
    if request.method == 'POST':
        form = FeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts')

    context = {'form': form}
    return render(request, 'sm/fees_form.html', context)
