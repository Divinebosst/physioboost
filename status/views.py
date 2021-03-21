from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from players.models import Player
from status.models import Status
from status_history.models import StatusHistory
from players import forms
from datetime import timedelta, date
from collections import Counter
from itertools import groupby
from collections import defaultdict

def status(request):
    player = Player.objects.all()
    return render(request, 'status/players.html', {'players':player})

@login_required(login_url="/account/login/")
def edit_player_status(request, slug):
    players = Player.objects.get(slug=slug)
    player_id = Player.objects.get(slug=slug).id
    form = forms.EditStatus(instance=players)
    if request.method == 'POST':
        form = forms.EditStatus(request.POST, instance=players)
        if form.is_valid():
            status_id = Status.objects.get(name=form.cleaned_data['status']).id
            status_history = StatusHistory(player_id = player_id, status_id=status_id)
            status_history.save()
            form.save()
            messages.success(request, 'Player status changed successfully!!!')
        else:
            messages.warning(request, 'Please correct the error below.') 
    return render(request, 'status/edit_players_status.html', {'form':form})

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield n+1

def tracker(request):
    players = Player.objects.all()
    pls = Player.objects.values('id').order_by('id')

    clist = range(1, ((abs(int((date.today().replace(day=1) - date.today()).days)) + 1)+1))
    clist = list(clist)
    #clist = [102, 232, 424]
    count = 0
    c = defaultdict(list)
    cnt = 0
    plss = defaultdict(list)
    for p in pls:
        plss[cnt] = p
        cnt+=1
        for n in clist:
            if not (StatusHistory.objects.raw("SELECT 1 as id, status_id FROM status_history_statushistory WHERE DAY(date)<=%s AND player_id=%s", [n, p['id']])):
                curday = StatusHistory.objects.raw("SELECT 1 as isd, players_player.name as name, players_player.surname as surname, id FROM players_player WHERE id=%s", [p['id']])
                for i in curday:
                    name = i.name
                    surname = i.surname
                    full_name = name + " " + surname
                    no_date = 5
                    c[full_name].append(no_date)
                    count+=1
                    
            if StatusHistory.objects.raw("SELECT 1 as id, status_id FROM status_history_statushistory WHERE DAY(date)=%s AND player_id=%s", [n, p['id']]):
                curday = StatusHistory.objects.raw("SELECT 1 as id, status_history_statushistory.status_id as status_id, players_player.name as name, players_player.surname as surname FROM status_history_statushistory LEFT JOIN players_player ON players_player.id=status_history_statushistory.player_id WHERE DAY(date)=%s AND player_id=%s", [n, p['id']])
                for i in curday:
                    name = i.name
                    surname = i.surname
                    full_name = name + " " + surname
                    c[full_name].append(i.status_id)
                    count+=1

            else:
                curday = StatusHistory.objects.raw("SELECT 1 as id, status_history_statushistory.status_id as status_id, players_player.name as name, players_player.surname as surname FROM status_history_statushistory LEFT JOIN players_player ON players_player.id=status_history_statushistory.player_id  WHERE DAY(date) < %s AND player_id=%s ORDER BY date DESC LIMIT 1", [n, p['id']]) 
                for i in curday:
                    name = i.name
                    surname = i.surname
                    full_name = name + " " + surname
                    c[full_name].append(i.status_id)
                    count+=1
            

            

    status_history = StatusHistory.objects.raw("SELECT DAY(date) as curday FROM status_history_statushistory LEFT JOIN players_player ON players_player.id=status_history_statushistory.player_id GROUP BY player_id")
    context = {'daterange': daterange(date.today().replace(day=1), date.today()),'daterange1': daterange(date.today().replace(day=1), date.today()), 'players':players, 'status_history':status_history, 'c':dict(c), 'p':pls, 'plss':plss}
    return render(request, 'status/tracker.html', context=context)
    
