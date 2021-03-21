from django.shortcuts import render, redirect
from . models import Injuries
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from .decorators import admin_required
from . import forms
from players.models import Player
import pandas as pd

# Create your views here.
@login_required(login_url="/account/login/")
def injury_view(request):
    injuries = Injuries.objects.all().order_by('date')
    return render(request, 'injuries/view_injuries.html', {'injuries':injuries})

@login_required(login_url="/account/login/")
def single_injuries(request, slug):
    injury = Injuries.objects.get(slug=slug)
    return render(request, 'injuries/single_injuries.html', {'injury':injury})

@admin_required
@login_required(login_url="/account/login/")
def add_injuries(request):
    if request.method == 'POST':
        form = forms.AddInjuries(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Injury added successfully!!!')
            return redirect('injuries:add_injury')
        else:
            messages.warning(request, 'Please correct the error below.') 
    else:
        form = forms.AddInjuries()
    return render(request, 'injuries/add_injuries.html', {'form':form})

@login_required(login_url="/account/login/")
@admin_required
def edit_injury(request, slug):
    players = Injuries.objects.get(slug=slug)
    form = forms.AddInjuries(instance=players)
    if request.method == 'POST':
        form = forms.AddInjuries(request.POST, instance=players)
        if form.is_valid():
            form.save()
            messages.success(request, 'Injury information changed successfully!!!')
        else:
            messages.warning(request, 'Please correct the error below.') 
    return render(request, 'injuries/edit_injuries.html', {'form':form})

@login_required(login_url="/account/login/")
def view_players(request):
    players = Player.objects.all()
    return render(request, 'injuries/view_players.html', {'players':players})

@login_required(login_url="/account/login/")
def predict_injury(request, slug):
    age = Player.objects.get(slug=slug).age
    weight = Player.objects.get(slug=slug).weight
    height = Player.objects.get(slug=slug).height
    players = Player.objects.get(slug=slug) #or any kind of queryset

    # Unpickle model 
    model = pd.read_pickle(r'c:\Users\Divine\Downloads\Compressed\YT-Django-Iris-App-3xj9B0qqps-master\new_model.pickle') 
    # read a pickle pd.read_pickle('model.pkl')
    #Make Prediction
    result = model.predict([[age,weight,height]])  # input must be 2D array

    classification = result[0]

    context = {'player':players, 'classification':classification}
    return render(request, 'injuries/predictions.html', context=context)

@login_required(login_url="/account/login/")
@admin_required
def delete_injury(request, id):
    p = Injuries.objects.get(pk=id)
    p.delete()
    return redirect('injuries:view_injuries')