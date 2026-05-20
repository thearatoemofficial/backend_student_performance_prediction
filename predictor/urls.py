# Import path for defining URL routes
from django.urls import path

# Import views from the current app
from . import views

# Define app-level URL patterns
urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
]
