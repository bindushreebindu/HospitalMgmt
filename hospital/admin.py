from django.contrib import admin
from .models import CardiologistDepartment
from .models import NeurologistDepartment
from .models import SurgeonDepartment
from .models import Doctor
from .models import Patient
from .models import *

# Register your models here.


class CardiologistDepartmentAdmin(admin.ModelAdmin):
	list_display=['doctor','patient','date1','time1']
	pass
class NeurologistDepartmentAdmin(admin.ModelAdmin):
	list_display=['doctor','patient','date1','time1']
	pass
class SurgeonDepartmentAdmin(admin.ModelAdmin):
	list_display=['doctor','patient','date1','time1']
	pass
class DoctorAdmin(admin.ModelAdmin):
	list_display=['name','mobile','special']

class PatientAdmin(admin.ModelAdmin):
	list_display=['name','gender','mobile','address']


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(CardiologistDepartment,CardiologistDepartmentAdmin)
admin.site.register(NeurologistDepartment,NeurologistDepartmentAdmin)
admin.site.register(SurgeonDepartment,SurgeonDepartmentAdmin)





