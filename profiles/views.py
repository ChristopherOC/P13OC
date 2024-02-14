"""
Fichier contenant les différentes vues de
l'application profiles
"""
from django.shortcuts import render
from .models import Profile
from django.http import Http404
from django.shortcuts import get_object_or_404


# Create your views here.
def profile(request, username):  # Vue de la page profile
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profile.html', context)
    except Http404:  # Lève une erreur 404 si le profile n'existe pas
        return render(request, '404.html', status=404)


def profiles_index(request):  # Vue détaillant les objets profiles
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)
