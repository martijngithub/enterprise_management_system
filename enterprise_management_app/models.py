from django.db import models

# Create your models here.

class Department(models.Model):
    main_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=30)
    dept_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

class Manager(models.Model):
    main_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE)
    designation = models.CharField(max_length=20)
    email = models.EmailField()
    gender_choices = (("1", "Male"), ("2", "Female"), ("3", "Other"))
    gender = models.CharField(choices=gender_choices, max_length=8, default=1)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

