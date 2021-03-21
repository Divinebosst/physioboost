from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import serializers
from players.models import Player
from stats.models import Stats
from django.contrib.auth.decorators import login_required
from . import forms
from django.shortcuts import get_object_or_404
from .decorators import admin_required
from django.db.models import Sum


# Create your views here.
@login_required(login_url="/account/login/")
def view_player(request):
    players = Player.objects.all() #or any kind of queryset
    return render(request, 'players/view_players.html', {'players':players})

@login_required(login_url="/account/login/")
def view_profile(request, slug):
    player_id = Player.objects.get(slug=slug).id
    #stats = Stats.objects.filter(player_id=player_id)
    #stats = Stats.objects.values('player_id', 'club_id','season').annotate(dgoals=Sum('goals'), dassists=Sum('assists')).filter(player_id=player_id)
    stats = Stats.objects.raw("SELECT 1 as id, SUM(goals) as dgoals, SUM(assists) as dassists, clubs_club.name as clubname, clubs_club.image as clubimage, club_id, season_id FROM  stats_stats LEFT JOIN clubs_club ON stats_stats.club_id=clubs_club.id WHERE player_id=%s GROUP BY club_id, season_id ORDER BY season_id DESC", [player_id])
    players = Player.objects.get(slug=slug) #or any kind of queryset
    context = {'player':players, 'stats':stats}
    return render(request, 'players/profile.html', context=context)

@login_required(login_url="/account/login/")
@admin_required
def add_player(request):
    if request.method == 'POST':
        form = forms.AddPlayer(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Player added successfully!!!')
            return redirect('players:add_player')
        else:
            messages.warning(request, 'Please correct the error below.') 
    else:
        form = forms.AddPlayer()
    return render(request, 'players/add_player.html', {'form':form})

@login_required(login_url="/account/login/")
@admin_required
def edit_player(request, slug):
    players = Player.objects.get(slug=slug)
    form = forms.AddPlayer(instance=players)
    if request.method == 'POST':
        form = forms.AddPlayer(request.POST,request.FILES, instance=players)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player information changed successfully!!!')
        else:
            messages.warning(request, 'Please correct the error below.') 
    return render(request, 'players/edit_player.html', {'form':form})

@login_required(login_url="/account/login/")
@admin_required
def delete_player(request, id):
    p = Player.objects.get(pk=id)
    p.delete()
    messages.warning(request, 'Player deleted!!!')
    return redirect('players:view')