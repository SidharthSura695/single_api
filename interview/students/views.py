from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import StudentMarks
import json

@csrf_exempt
def store_marks(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student, created = StudentMarks.objects.update_or_create(
                student_id=data['student_id'],
                defaults={'marks': data['marks']}
            )
            return JsonResponse({'message': 'Marks stored successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


def is_third_highest(request, student_id):
    try:
        marks_list = list(StudentMarks.objects.values_list('marks', flat=True).distinct().order_by('-marks'))
        if len(marks_list) < 3:
            return JsonResponse({'result': False, 'reason': 'Less than 3 unique marks available'})
        third_highest = marks_list[2]
        student = get_object_or_404(StudentMarks, student_id=student_id)
        return JsonResponse({'result': student.marks == third_highest})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)