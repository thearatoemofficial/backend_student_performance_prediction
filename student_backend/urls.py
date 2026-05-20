#import admin route support
from django.contrib import admin

#import path and include URL routing
from django.urls import path, include

#Define the main project URL patterns
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', include('predictor.urls')),
]