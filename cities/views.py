from typing import Dict, Any

from django.shortcuts import render, get_object_or_404

from .models import City

__all__ = (
    'home',
)

def home(request, pk=None):
    if pk:
        # city = City.objects.filter(id=pk).first()
        # city = City.objects.get(id=pk)
        city = get_object_or_404(City, id=pk)

        context: dict[str, Any] = {'object': city}
        return render(request, 'cities/detail.html', context)
    cities = City.objects.all()
    context: dict[str, Any] = {'objects_list': cities}
    return render(request, 'cities/home.html', context)
