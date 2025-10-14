from django.shortcuts import render
from django.contrib.auth.forms import
AuthenticationForm

def homepage(request):
form = AuthenticationForm(request)
return render(request,'homepage.html',{'form':form})