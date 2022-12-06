import sqlite3

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.db import connection, transaction

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from .models import Shout
from django import forms
from .forms import ShoutForm
from django.utils import timezone

# Create your views here.

def index(request):
	return redirect('shouts')

def shouts(request):
	shoutList = Shout.objects.all()
	return render(request, 'shouts/index.html',{'shoutList':shoutList,})

# @login_required
def addShout(request):

	new_shout_text = request.POST.get('shout_text')
	new_shout_author = request.POST.get('shout_author')
	time_now = timezone.now()

	query = "INSERT INTO shouts_shout (shout_text, author_text, pub_date) VALUES('%s', '%s', '%s');" % (new_shout_text, new_shout_author, time_now)
	database = 'db.sqlite3'
	conn = sqlite3.connect(database)
	cursor = conn.cursor()

	response = cursor.executescript(query) 
	# executescript() -> execute() , execute() will only do one query	

	return redirect('home')



def detail(request, shout_id):
	shout = get_object_or_404(Shout, pk=shout_id)
	return render(request, 'shouts/detail.html',
                  {'shout': shout})

# @login_required
def home(request):
	shoutList = Shout.objects.all()
	form = ShoutForm()
	return render(request, 'shouts/home_loggedin.html', {'shoutList':shoutList, 'shoutForm':form})

def logout_app(request):
    logout(request)
    return redirect('shouts')









