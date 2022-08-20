from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
"""
Serialization Operation - Django Rest Framework
"""

# Model Object -  Single Student Data
def stdent_detail(request, pk):
    stu = Student.objects.get(id = pk)
    print("stu:", stu)  # for debug purpose.. to check in terminal
    serializer = StudentSerializer(stu)
    print("serializer: ",serializer)  # for debug purpose.. to check in terminal
    print("serializer data: ",serializer.data)  # for debug purpose.. to check in terminal
    """
    json_data = JSONRenderer().render(serializer.data)
    print("JSON Data: ",json_data)  # for debug purpose.. to check in terminal
    return  HttpResponse(json_data, content_type='application/json')
    
    we can replace this code with "return JsonResponse(serializer.data)"
    """
    return JsonResponse(serializer.data, safe=True)


# Query Set -  list of Students Data
def stdent_list(request):
    stu = Student.objects.all()
    print("stu:", stu)  # for debug purpose.. to check in terminal
    serializer = StudentSerializer(stu, many=True)
    print("serializer: ",serializer)  # for debug purpose.. to check in terminal
    print("serializer data: ",serializer.data)  # for debug purpose.. to check in terminal

    """
    json_data = JSONRenderer().render(serializer.data)
    print("JSON Data: ",json_data)  # for debug purpose.. to check in terminal
    return  HttpResponse(json_data, content_type='application/json')
    
    we can replace this code with "return JsonResponse(serializer.data)"
    
    """
    return JsonResponse(serializer.data, safe=False)
