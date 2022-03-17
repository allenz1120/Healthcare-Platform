from django.contrib import admin
from .models import Users, Billing, Medical_History, Role_Relation, Roles, Device_Blood_Pressure, Device_Thermometer

# Register your models here.
admin.site.register(Users)
admin.site.register(Billing)
admin.site.register(Medical_History)
admin.site.register(Role_Relation)
admin.site.register(Roles)
admin.site.register(Device_Blood_Pressure)
admin.site.register(Device_Thermometer)
