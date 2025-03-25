from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import request
from .models import Student
from django.urls import reverse
from .forms import StudentForm
# Create your views here.

def index(request):
   return render(request, "students/index.html", {
      'students': Student.objects.all(),
   })
def view_student(request, id):
   student = Student.objects.get(id=id)
   return HttpResponseRedirect(reverse('index'))

def add_student(request):
   if request.method == "POST":
      form = StudentForm(request.POST)
      if form.is_valid():
         new_student_id = form.cleaned_data['student_id']
         new_first_name = form.cleaned_data['first_name']
         new_last_name = form.cleaned_data['last_name']
         new_email = form.cleaned_data['email']
         new_field_of_study = form.cleaned_data['field_of_study']
         new_gpa = form.cleaned_data['gpa']
         new_student = Student(
            student_id=new_student_id,
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,
            field_of_study=new_field_of_study,
            gpa=new_gpa,
         )
         new_student.save()
         return render(request,'students/add.html', {
            'form': StudentForm(),
            'success': True,
         })
   else:
      form = StudentForm()
      return render(request,'students/add.html', {
         'form': StudentForm(),
      })
def edit_student(request, id):
   if request.method == "POST":
      student = Student.objects.get(id=id)
      form = StudentForm(request.POST, instance=student)
      if form.is_valid():
         form.save()
         return render(request,'students/edit.html', {
            'form':form,
            'success': True,
         })
   else:
      student = Student.objects.get(id=id)
      form = StudentForm(instance=student)
      return render(request,'students/edit.html', {
         'form':form,
      })

def delete_student(request, id):
   if request.method == "POST":
      student = Student.objects.get(id=id)
      student.delete()
   return HttpResponseRedirect(reverse('index'))



