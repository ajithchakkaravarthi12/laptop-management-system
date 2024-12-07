from django.db import models
class Laptop(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model}"



class Assignment(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title



class Employee(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=100)


class Maintenance(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    maintenance_date = models.DateField()
    description = models.TextField()

class Issue(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
