#Import Json for JSON processing
import json
#Import JsonResponse to return JSON data to the client
from django.http import JsonResponse

#Import csrf_exempt to simplify API testing during development
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    #Return a simple message for the root route
    return JsonResponse({
        'message':'Django Student Prediction API is Running...'
    })
@csrf_exempt
def predict(request):
    #Allow only POST request on this route
    if request.method != 'POST':
        return JsonResponse({
            'error':'Only POST method is allowed.'
        }, status = 405)
    #Return a temporary message showing the endoint is ready
    return JsonResponse({
        'message':'Predict endpoint is ready'
    })
