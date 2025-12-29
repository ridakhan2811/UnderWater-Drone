# team/views.py
from django.shortcuts import render, get_object_or_404
from .models import TeamMember

def team(request):
    members = TeamMember.objects.all()
    leaders = members.filter(role='leader')
    engineers = members.exclude(role='leader')
    
    context = {
        'leaders': leaders,
        'engineers': engineers,
        'total_members': members.count(),
    }
    return render(request, 'team/team.html', context)

def member_detail(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    context = {'member': member}
    return render(request, 'team/member_detail.html', context)

