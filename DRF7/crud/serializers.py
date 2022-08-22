from rest_framework import serializers
from .models import Student

"""
************ ModelSerializer ****************
we will use third party application to perform operation 
in this case we will use myapp.py file 
"""


class StudentSerializer(serializers.ModelSerializer):
    """
    to add argument to particular field there are 3 ways
    1) write particular fields and apply arguments on them:
    exp:- name = serializers.CharField(read_only=True)

    2) apply single argument on multiple fields:
    syn- argument_fields = ['field1', 'field2']
    exp- read_only_fields = ['name','roll']

    3) apply multiple arguments in multiple fields
    syn- extra_kwargs = {'field' : {'argument': Value}}
    exp- extra_kwargs = {'name': {'read_only': True}}
    """
    # 1) apply read_only argument on name
    # name = serializers.CharField(read_only=True)

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
        # 2) apply read only on multiple field - add fields in list
        # read_only_fields = ['roll']

        # 3) Apply multiple arguments on multiple fields
        extra_kwargs = {'name': {'read_only': True}}
