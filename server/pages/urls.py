# yourapp/urls.py
from django.urls import path
#from .views import login_view
from .views import home_view

urlpatterns = [
    path('home/', home_view, name='home'),
    path('', home_view, name='home'),
]
