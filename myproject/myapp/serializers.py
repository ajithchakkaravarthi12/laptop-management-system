from rest_framework import serializers
from .models import Laptop, Employee, Assignment, Maintenance, Issue

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    laptop = LaptopSerializer()
    employee = EmployeeSerializer()

    class Meta:
        model = Assignment
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    laptop = LaptopSerializer()

    class Meta:
        model = Maintenance
        fields = '__all__'

class IssueSerializer(serializers.ModelSerializer):
    laptop = LaptopSerializer()
    reported_by = EmployeeSerializer()

    class Meta:
        model = Issue
        fields = '__all__'
        
class Assignment(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Additional fields
