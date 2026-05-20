# Import json for parsing JSON request bodies
import json

# Import JsonResponse to return JSON output
from django.http import JsonResponse

# Import csrf_exempt for simpler API testing during development
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
    # Return an API status message
    return JsonResponse({
        'message': 'Django Student Prediction API is running'
    })


@csrf_exempt
def predict(request):
    # Allow only POST requests
    if request.method != 'POST':
        return JsonResponse({
            'error': 'Only POST method is allowed'
        }, status=405)

    # Parse the incoming JSON request body
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'Invalid JSON format'
        }, status=400)

    # Check whether the request body is empty
    if not data:
        return JsonResponse({
            'error': 'No data provided'
        }, status=400)

    # Define the required fields
    required_fields = [
        'student_name',
        'age',
        'study_hours',
        'attendance',
        'previous_grade',
        'assignments_completed'
    ]

    # Check for missing fields
    for field in required_fields:
        if field not in data:
            return JsonResponse({
                'error': f'Missing field: {field}'
            }, status=400)

    # Extract the input values
    student_name = data.get('student_name')
    age = data.get('age')
    study_hours = data.get('study_hours')
    attendance = data.get('attendance')
    previous_grade = data.get('previous_grade')
    assignments_completed = data.get('assignments_completed')

    # Validate student_name
    if not isinstance(student_name, str) or not student_name.strip():
        return JsonResponse({
            'error': 'student_name must be a non-empty string'
        }, status=400)

    # Convert numeric fields to numbers
    try:
        age = float(age)
        study_hours = float(study_hours)
        attendance = float(attendance)
        previous_grade = float(previous_grade)
        assignments_completed = float(assignments_completed)
    except (TypeError, ValueError):
        return JsonResponse({
            'error': 'age, study_hours, attendance, previous_grade, and assignments_completed must be numeric'
        }, status=400)

    # Validate numeric ranges
    if age <= 0:
        return JsonResponse({
            'error': 'age must be greater than 0'
        }, status=400)

    if study_hours < 0:
        return JsonResponse({
            'error': 'study_hours cannot be negative'
        }, status=400)

    if attendance < 0 or attendance > 100:
        return JsonResponse({
            'error': 'attendance must be between 0 and 100'
        }, status=400)

    if previous_grade < 0 or previous_grade > 100:
        return JsonResponse({
            'error': 'previous_grade must be between 0 and 100'
        }, status=400)

    if assignments_completed < 0:
        return JsonResponse({
            'error': 'assignments_completed cannot be negative'
        }, status=400)

    # Apply rule-based prediction logic
    if (
        study_hours >= 8 and
        attendance >= 80 and
        previous_grade >= 75 and
        assignments_completed >= 8
    ):
        prediction = 'Excellent'
    elif (
        study_hours >= 5 and
        attendance >= 60 and
        previous_grade >= 50 and
        assignments_completed >= 5
    ):
        prediction = 'Good'
    else:
        prediction = 'Needs Improvement'

    # Return the final prediction result
    return JsonResponse({
        'student_name': student_name,
        'prediction': prediction
    })
