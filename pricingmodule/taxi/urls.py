from nturl2path import url2pathname
from django.urls import  path
from .views import TripCost,RatesView

urlpatterns = [
    path('rates/',RatesView,name='rates-view'),
    path('price/',TripCost.as_view()),
]