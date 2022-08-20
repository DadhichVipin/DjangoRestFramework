from rest_framework import serializers
from .models import Student

"""
************ ModelSerializer ****************
we will use third party application to perform operation 
in this case we will use myapp.py file 
"""


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        """
        We can Define list of filed you want
        fields = ['id', 'name', 'roll', 'city']
        *********** or **********
        we can define all fields using __all__
        fields = '__all__'
        *********** or **********
        we can exclude any field
        exclude = ['roll']
        """
        fields = ['name', 'roll', 'city']
