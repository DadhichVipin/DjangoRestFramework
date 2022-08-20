import io

from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

"""
We will perform Deserialization operation

We will create/ Insert data through third party application. 
In this case we will insert through appToIntrectWithDRF2.py file 
located in  DRF2 project(this file can be located any where).
"""


@csrf_exempt  # to add csrf token
def student_create(request):
    if request.method == 'POST':
        json_data = request.body  # requesting JSON data
        print(request.body)
        stream = io.BytesIO(json_data)  # converting json data into stream
        print(stream)
        python_data = JSONParser().parse(stream)  # converting data into python netive
        print(python_data)
        serializer = StudentSerializer(data=python_data)  # De-serialization (converting python data to complex data).
        print(serializer)
        if serializer.is_valid():  # check data is valid or not
            serializer.save()  # if valid than save in database
            res = {'msg': 'Data Created'}  # response/ msg
            json_data = JSONRenderer().render(res)  # render msg/ response when data inserted
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)  # catch the error if data is not valid
        return HttpResponse(json_data, content_type='application/json')
