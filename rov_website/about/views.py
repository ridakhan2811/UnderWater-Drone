
# about/views.py
from django.shortcuts import render
from .models import Vehicle

def about(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles,
        'team_info': {
            'members': 3,
            'lines_of_code': 55000,
            'years': '2024-2026',
        }
    }
    return render(request, 'about/about.html', context)

def subdivisions(request):
    subdivisions = Subdivision.objects.all()
    context = {'subdivisions': subdivisions}
    return render(request, 'about/subdivisions.html', context)





