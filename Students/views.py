
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
# Create your views here.
from .models import Student

class RegisterForm(forms.ModelForm):
	"""docstring for Register"""
	class Meta:
		model=Student
		items='__all__'

def Register(request):
	if request.method=='POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			s=Student.objects.get(idnum=form.cleaned_data['idnum'])
			if not s:
				form.save()
				return HttpResponseRedirect('/')
			else:
				print form.cleaned_data
	else:
		form = RegisterForm()
	return render(request,'register.html',{'form':form})

def GetId(request):
	try:
		student = Student.objects.get(idnum=request.GET.get('student_id', "B091234"))
	except:
		student = "no"
	return render(request, 'student.html', {'student': student})

def home(request):
	return render(request, 'base.html')