from rest_framework import serializers
from .models import Student

"""
we will use third party application to perform operation 
in this case we will use myapp.py file 


***** Field level Validation *****
***** Object level Validation *****
***** Validators Validation *****
"""


# validator
def start_with_uppercase(value):
    if value[0].isupper():
        return value
    else:
        raise serializers.ValidationError('Should Start with Uppercase')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_uppercase])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field Level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full... ")
        return value

    # Object Level Validation
    def validate(self, data):
        nam = data.get('name')
        city = data.get('city')

        if nam.islower() or city.islower():
            raise serializers.ValidationError("Name and City can not be in lower case")
        return data


