# django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# django-rest-framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# app
from . import models
from . import serializers

# Create your views here.

def index(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')




@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def showEmployee(request):
    employeeSerializer = serializers.EmployeeSerializer(models.Employee.objects.all().order_by('department'), many=True).data
    data =[]
    for item in employeeSerializer:
        item = dict(item)
        
        item['department'] = models.Department.objects.get(id=int(item['department'])).department
        data.append(item)
    
    
    return Response(
        {
            "status":True,
            "data":data
        }
    )
    
@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def showDepartment(request):
    data = serializers.DepartmentSerializer(models.Department.objects.all(), many=True).data
    
    return Response(
        {
            "status":True,
            "data":data
        }
    )
    

@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def EmployeeFilter(request):
    id = request.data['id']
    employeeSerializer = serializers.EmployeeSerializer(models.Employee.objects.filter(department=id), many=True).data
    data =[]
    for item in employeeSerializer:
        item = dict(item)
        
        item['department'] = models.Department.objects.get(id=int(item['department'])).department
        data.append(item)
    
    return Response(
        {
            "status":True,
            "data":data
        }
    )