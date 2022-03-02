from django.contrib import admin
from .models import Users, Billing, Medical_History

# Register your models here.
admin.site.register(Users)
admin.site.register(Billing)
admin.site.register(Medical_History)
