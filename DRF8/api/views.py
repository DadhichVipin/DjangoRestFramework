from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
"""
*************** DRF function based view - @api_view ******************
function based view 
DRF's @api_view gives us browsable api view 

*** GET ***
@api_view()
def hello(request):
    return Response({'msg':'Hello Boss'})
    
*** POST ***
@api_view(['POST'])
def hello(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Hello Boss...this is post request'})

*** GET & POST in one ***
@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response({'msg':'Hello Boss...this is GET request'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Hello Boss...this is post request', 'data': request.data})
"""
"""
Put - Complete update
patch - partial update
"""

@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        stu = Student.objects.get(pk= pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        stu = Student.objects.get(pk= pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        stu = Student.objects.get(pk= pk)
        stu.delete()
        return Response({'msg':'Data Deleted'})
