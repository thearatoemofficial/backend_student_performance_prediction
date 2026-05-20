# Import admin route support
from django.contrib import admin

# Import path and include for URL routing
from django.urls import path, include

# Define the main project URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predictor.urls')),
]
