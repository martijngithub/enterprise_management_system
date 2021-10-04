from django.db import models

# Create your models here.

class Department(models.Model):
    main_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=30)
    dept_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
        
    def __str__(self):
        return f'{self.main_id} {self.dept_name}'

class Manager(models.Model):
    main_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE, default=1)
    designation = models.CharField(max_length=20)
    email = models.EmailField()
    gender_choices = (("1", "Male"), ("2", "Female"), ("3", "Other"))
    gender = models.CharField(choices=gender_choices, max_length=8, default=1)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.main_id} {self.name}'

class Employee(models.Model):
    main_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE, default=1)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE, default=1)
    designation = models.CharField(max_length=20)
    email = models.EmailField()
    gender_choices = (("1", "Male"), ("2", "Female"), ("3", "Other"))
    gender = models.CharField(choices=gender_choices, max_length=8, default=1)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.main_id} {self.name}'

class Clerk(models.Model):
    main_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    dept = models.ForeignKey(Department, on_delete = models.CASCADE, default=1)
    manager = models.ForeignKey(Manager, on_delete = models.CASCADE, default=1)
    designation = models.CharField(max_length=20)
    email = models.EmailField()
    gender_choices = (("1", "Male"), ("2", "Female"), ("3", "Other"))
    gender = models.CharField(choices=gender_choices, max_length=8, default=1)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.main_id} {self.name}'

class ProductCategory(models.Model):
    main_id = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length = 30)
    product_category_desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.main_id} {self.product_category_name}'

class Product(models.Model):
    main_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 30)
    product_desc = models.TextField()
    product_price = models.FloatField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.main_id} {self.product_name}'


   

