from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Department
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Employee
        fields = '__all__'