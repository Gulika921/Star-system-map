from django.shortcuts import render, get_object_or_404
from starsystem.models import Galaxy

# Create your views here.

def galaxy_view(request, obj=None):
    galaxy = get_object_or_404(Galaxy, pk=obj)
    context = {
        "galaxy": galaxy
    }
    return render(request,"galaxy.html", context)