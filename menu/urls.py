from . import views

from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
path('meenu', views.menu,name='meenu'),

path('Sweets', views.Sweets,name='Sweets'),

path('IceCream', views.IceCream,name='IceCream'),

path('PartyBox', views.PartyBox,name='PartyBox')

]
urlpatterns += staticfiles_urlpatterns()