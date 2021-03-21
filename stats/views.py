from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from players.models import Player
from stats.models import Stats
from season.models import Season


def stats(request):
    player = Player.objects.all()
    return render(request, 'stats/players.html', {'players':player})

@login_required(login_url="/account/login/")
def add_stats(request, slug):
    player_id = Player.objects.get(slug=slug).id
    club_id = Player.objects.get(slug=slug).club_id
    season = Season.objects.values('id').order_by('-id')[:1]
    if request.method == 'POST':
        form = forms.AddStats(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.player_id = player_id
            instance.club_id = club_id
            instance.author = request.user
            instance.season_id = season
            instance.save()
            messages.success(request, 'Player stats added successfully!!!')
            return redirect('stats:players')
        else:
            messages.warning(request, 'Please correct the error below.') 
    else:
        form = forms.AddStats()
    return render(request, 'stats/add_stats.html', {'form':form})

@login_required(login_url="/account/login/")
def edit_stats(request, id):
    stat_id = Stats.objects.get(id=id)
    form = forms.AddStats(instance=stat_id)
    if request.method == 'POST':
        form = forms.AddStats(request.POST, instance=stat_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player stats changed successfully!!!')
            return redirect('stats:players')
        else:
            messages.warning(request, 'Please correct the error below.') 
    return render(request, 'stats/edit_stats.html', {'form':form})

def delete_stats(request, id):
    p = Stats.objects.get(pk=id)
    p.delete()
    return redirect('stats:players')

@login_required(login_url="/account/login/")
def history_stats(request, slug):
    player_id = Player.objects.get(slug=slug).id
    player_name = Player.objects.get(slug=slug).name
    player_image = Player.objects.get(slug=slug).image
    player_surname = Player.objects.get(slug=slug).surname
    stats = Stats.objects.filter(player_id=player_id)
    context = {'stats':stats, 'player_name':player_name, 'player_surname':player_surname, 'player_image':player_image}
    return render(request, 'stats/view_history.html', context=context)

