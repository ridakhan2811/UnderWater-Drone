# home/views.py
from django.shortcuts import render
from about.models import Vehicle
from home.models import ProjectInfo

def index(request):
    try:
        project_info = ProjectInfo.objects.first()
    except:
        project_info = None
    
    vehicles = Vehicle.objects.all()
    featured_vehicles = vehicles[:3]
    
    context = {
        'project_info': project_info,
        'featured_vehicles': featured_vehicles,
        'total_vehicles': vehicles.count(),
    }
    return render(request, 'home/index.html', context)

def vehicles(request):
    vehicles = Vehicle.objects.all()
    context = {'vehicles': vehicles}
    return render(request, 'home/vehicles.html', context)

