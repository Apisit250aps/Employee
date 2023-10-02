from django.db import models

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=128)
    
    def __str__(self):
        return self.department
    
class Employee(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=16, choices=(
        ("ชาย", "ชาย"),
        ("หญิง", "หญิง")
    ))
    age = models.IntegerField()
    education = models.CharField(max_length=64, choices=(
        ("ปวช.", "ปวช."),
        ("ปวส.", "ปวส."),
        ("ปริญญาตรี", "ปริญญาตรี"),
        ("สูงกว่าปริญญาตรี", "สูงกว่าปริญญาตรี)")
    ))
    department =models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.fname} {self.lname} : {self.department}"
    
