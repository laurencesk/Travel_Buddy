from __future__ import unicode_literals
from django.shortcuts import render,redirect, HttpResponse
from .models import User,UserManager,Trip,TripManager
import bcrypt
from django.contrib import messages
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request,'travel_buddy/index.html')

def register(request):
    u = User.objects.filter(username=request.POST['username'])
    if len(u)!=0:
        messages.warning(request,"You have already registered")
        return redirect('/')
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        bc_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name = request.POST['name'], username = request.POST['username'], password = bc_password)
        user.save()
        request.session['id'] = user.id
        return redirect('/dashboard')

def login(request):
    request.session.flush()
    if len(User.objects.filter(username=request.POST['username'])) == 0:
        messages.warning(request,"The information you entered do not match our records")
        return redirect('/')
    elif bcrypt.checkpw(request.POST['password'].encode(), User.objects.get(username=request.POST['username']).password.encode()):
        user = User.objects.get(username = request.POST['username'])
        request.session['id'] = user.id
        return redirect("/dashboard")
    else:
        messages.warning(request,"The information you entered do not match our records")
        return redirect('/')

def dashboard(request):
    if request.session['id']:
        context={
            'user': User.objects.get(id = request.session['id']),
            'schedule': Trip.objects.filter(Q(planned_by_id = request.session['id']) | Q(joined_by=request.session['id'])),
            'trips':Trip.objects.exclude(Q(planned_by_id = request.session['id']) | Q(joined_by=request.session['id']))
        }
    return render(request,"travel_buddy/dashboard.html",context)

def add(request):
    return render(request,"travel_buddy/add.html")

def new_trip(request):

    errors = Trip.objects.Trip_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add')
    
    user = User.objects.get(id=request.session['id'])
    destination = request.POST['destination']
    description = request.POST['description']
    trave_start_date = request.POST['trave_start_date']
    trave_end_date = request.POST['trave_end_date']

    trip = Trip.objects.get_or_create(destination =destination, description= description,trave_start_date = trave_start_date, trave_end_date = trave_end_date, planned_by = user)
    return redirect('/dashboard')

def destination(request,id):
    trip = Trip.objects.get(id = id)
    context={
        'trip': Trip.objects.get(id = id),
        'join': trip.joined_by.exclude(id = id)

    }
    return render(request,"travel_buddy/destination.html",context)

def join(request,id):
    user = User.objects.get(id = request.session['id'])
    trip = Trip.objects.get(id = id)
    trip.joined_by.add(user)
    return redirect('/dashboard')


def logout(request):
    request.session.flush()
    return redirect("/")