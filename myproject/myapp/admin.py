from django.contrib import admin
from .models import Laptop, Employee, Assignment, Maintenance, Issue

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['laptop', 'employee', 'title']
    search_fields = ['laptop__brand', 'employee__name', 'title']


admin.site.register(Laptop)
admin.site.register(Employee)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Maintenance)
admin.site.register(Issue)
