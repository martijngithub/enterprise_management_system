from django.contrib import admin
from enterprise_management_app import models

# Register your models here.
admin.site.register(models.Department)
admin.site.register(models.Manager)
admin.site.register(models.Employee)
admin.site.register(models.Clerk)
admin.site.register(models.ProductCategory)
admin.site.register(models.Product)