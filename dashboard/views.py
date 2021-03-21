from django.shortcuts import render
from clubs.models import Club
from players.models import Player
from assessment.models import Assessment
from injuries.models import Injuries
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

# Create your views here.
@login_required(login_url="/account/login/")
def dashboard(request):
    players = Player.objects.all()
    avg_age = Player.objects.filter(club=request.user.club).aggregate(Avg('age'))
    avg_height = Player.objects.filter(club=request.user.club).aggregate(Avg('height'))
    avg_weight = Player.objects.filter(club=request.user.club).aggregate(Avg('weight'))
    injuries = Injuries.objects.all()
    assessments = Assessment.objects.filter(author_id=request.user.id)
    previous_assessments = Assessment.objects.filter(author_id=request.user.id)
    context = {'player':players, 'injury':injuries, 'assessment':assessments, 'avgage':avg_age, 'avgheight':avg_height, 'avgweight':avg_weight, 'previous_assessment': previous_assessments}
    return render(request, 'dashboard/dashboard.html', context=context)