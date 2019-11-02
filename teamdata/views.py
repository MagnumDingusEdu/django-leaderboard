from django.shortcuts import render
from .models import Team

# Create your views here.

def leader_view(request, *args, **kwargs):

    team_list = Team.objects.order_by('-marks')
    cleaned_list = []

    context = {
        'teamlist':team_list,
    }
    return render(request, 'teamdata/index.html', context)