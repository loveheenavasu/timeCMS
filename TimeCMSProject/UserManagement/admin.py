from django.contrib import admin
from .models import Users,Address, Roles, Permission
# Register your models here.
admin.site.register(Users)
admin.site.register(Address)
admin.site.register(Roles)
admin.site.register(Permission)

