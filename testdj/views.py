#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	return redirect("blog/")

def home_files(request, filename):
	return render(request, filename, {}, content_type="text/plain")