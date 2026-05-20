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
    #Allow only POST request
    if request.method != 'POST':
        return JsonResponse({
            'error':'Only POST method is allowed'
        }, status = 405)
    #Attempt to read and parse JSON data from the request body
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        #Return an error if the request body is invalid JSON
        return JsonResponse({
            'error':'Invalid JSON format'
        }, status = 400)
     
    #Check whether any data was provided
    if not data:
        return JsonResponse({
            'error':'No data provided'
        }, status = 400)
    #Define the require fields for the preduction
    required_fields = ['study_hours', 'attendance', 'assignment_completed']

    #Check whether each required fields exists
    for field in required_fields:
        if field not in data:
            return JsonResponse({
                'error':f'Missing field:{field}'
            }, status = 400)
    #Extract values from the JSON data
    study_hours = data.get('study_hours')
    attendance  = data.get('attendance') 
    assignment_completed = data.get('assignment_completed')

    #Try to converting values to numbers
    try:
        study_hours = float(study_hours)
        attendance  = float(attendance)
        assignment_completed = float(assignment_completed)
    except (TypeError, ValueError):
        return JsonResponse ({
            'error':'study_hours, attendance and assignment_completed must be numberic'
        } ,status = 400)   
    #Return a temporary success message after validation
    # return JsonResponse({
    #     'message':'Validation passed',
    #     'study_hours': study_hours,
    #     'attendance': attendance,
    #     'assignment_completed': assignment_completed
    # })

    #Apply rule-based predic logic
    if study_hours >= 8 and attendance >= 80 and assignment_completed >= 8:
        prediction = 'Excellent'
    else:
        prediction = 'Need Improvement'
    return JsonResponse({
        'Prediction': prediction
    })        