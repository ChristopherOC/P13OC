from django.shortcuts import render
from .models import Letting

from django.http import Http404
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)

def letting(request, letting_id):
    try :
        letting = get_object_or_404(Letting,id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'letting.html', context)
    except Http404:
        return render(request, '404.html', status=404)
    

def custom_404(request, *args, **kwargs):
    return render(request, '404.html', status=404)

def erreur_404(request):
    raise Http404("Cette page n'existe pas")

def custom_500(request):
    return render(request, '500.html', status=500)

