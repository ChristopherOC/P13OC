from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404, handler500

import letting.views
import profiles.views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', letting.views.index, name='index'),
    path('lettings/', letting.views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting.views.letting, name='letting'),
    path('profiles/', profiles.views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('custom_404/', letting.views.custom_404, name='custom_404'),
    path('error_404/', letting.views.erreur_404, name='error_404'),
    path('error_500/', letting.views.custom_500, name='custom_500')
]

handler404 = letting.views.custom_404
handler500 = letting.views.custom_500
