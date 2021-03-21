from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Assessment
from players.models import Player
from dataset.models import Dataset
from .decorators import admin_required
from diagnosis.models import Diagnosis

@login_required(login_url="/account/login/")
def assess(request):
    assessments = Assessment.objects.all()
    return render(request, 'assessment/view_assessment.html', {'assessments':assessments})

@login_required(login_url="/account/login/")
def player_assessment(request):
    player =   Player.objects.all()
    return render(request, 'assessment/player_assessment.html', {'players':player})

@login_required(login_url="/account/login/")
def add_assessment(request, slug):
    if 'term' in request.GET:
        qs = Diagnosis.objects.filter(name__istartswith=request.GET.get('term')) | Diagnosis.objects.filter(code__istartswith=request.GET.get('term'))
        names = list()
        for name in qs:
            names.append(name.code + " - " + name.name)
        return JsonResponse(names, safe=False)
        
    player_slug = Player.objects.get(slug=slug).slug
    player_name = Player.objects.get(slug=player_slug).name
    player_surname = Player.objects.get(slug=player_slug).surname
    player_age = Player.objects.get(slug=player_slug).age
    player_weight = Player.objects.get(slug=player_slug).weight
    player_height = Player.objects.get(slug=player_slug).height
    if request.method == 'POST':
        form = forms.AddAssessment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = player_name
            instance.surname = player_surname
            instance.author = request.user
            #dataset = Dataset(age=player_age, weight=player_weight, height=player_height, classification=form.cleaned_data['injury'])
            #dataset.save()
            instance.save()
            form.save_m2m()
            messages.success(request, 'Player assessed successfully!!!')
            return redirect('assessment:player_assessment')
        else:
            messages.warning(request, 'Please correct the error below.') 
    else:
        form = forms.AddAssessment()
    return render(request, 'assessment/add_assessment.html', {'form':form})

@login_required(login_url="/account/login/")
@admin_required
def edit_assessment(request, slug):
    assessment = Assessment.objects.get(id=slug)
    form = forms.AddAssessment(instance=assessment)
    if request.method == 'POST':
        form = forms.AddAssessment(request.POST, instance=assessment)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            messages.success(request, 'Assessment information changed successfully!!!')
        else:
            messages.warning(request, 'Please correct the error below.') 
    return render(request, 'assessment/edit_assessment.html', {'form':form})

@login_required(login_url="/account/login/")
def single_assessment(request, id):
    assessment = Assessment.objects.get(id=id)
    return render(request, 'assessment/single_assessment.html', {'assessment':assessment})