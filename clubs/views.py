from django.shortcuts import render
from clubs.models import Club
from players.models import Player

# Create your views here.
def view_clubs(request, id):
    clubs = Club.objects.get(id=id)
    club_id = Club.objects.get(id=id).id
    goalkeepers = Player.objects.filter(club_id=club_id, position_id=1)
    defenders = Player.objects.filter(club_id=club_id, position_id=2)
    midfielders = Player.objects.filter(club_id=club_id, position_id=3)
    forwards = Player.objects.filter(club_id=club_id, position_id=4)
    context = {'clubs':clubs, 'goalkeepers':goalkeepers, 'defenders':defenders, 'midfielders':midfielders, 'forwards':forwards}
    return render(request, 'clubs/view_clubs.html', context=context)

