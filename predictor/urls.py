#import path for defining URL routes
from django.urls import path

#import views from the current app
from . import views

#Define app-lelvel URL patterns
urlpatterns = [
    path('', views.home, name= 'home'),
    path('predict/', views.predict , name= 'predict'),
]