from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

"""
CRUD Operations - Django Rest Framework
"""

@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type="application/json")
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="application/json")

    elif request.method == 'PUT':
        """ Partial Update """
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        """ for partial Update - (update only some fields )- 
        we need to pass 'partial = True' argument with serializer 
        of complete update we need to remove 'partial = True' 
        
        if there is no 'partial = True' argument then it will request to pass all fields for update """
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data is Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="application/json")

    elif request.method == 'DELETE':
        """ Delete the data """
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg': 'Data is Deleted'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type="application/json")
