from django.urls import path
from enterprise_management_app import views

urlpatterns = [
    path("", views.render_login, name="render_login"),
    path("perform_login", views.perform_login, name="perform_login"),
    path("perform_logout", views.perform_logout, name="perform_logout"),
    path("index/", views.index, name = "index"),
    path("departments/", views.departments, name = "departments"),
    path("managers/", views.managers, name = "managers"),
    path("employees/", views.employees, name = "employees"),
    
]
