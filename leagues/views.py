from django.shortcuts import render
from leagues.models import Leagues
from clubs.models import Club

# Create your views here.
def view_leagues(request):
    leagues = Leagues.objects.all()
    clubs = Club.objects.all()
    context = {'leagues':leagues, 'clubs':clubs}
    return render(request, 'leagues/view_leagues.html', context=context)

