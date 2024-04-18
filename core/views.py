from django.shortcuts import render
from .models import Vehicle

# Create your views here.
def index(request):
    context = {'Vehicle': list(Vehicle.objects.values('latitude', 'longitude'))}
    return render(request, 'index.html', context)