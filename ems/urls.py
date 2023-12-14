from django.contrib import admin
from django.urls import path
from ems_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.e_login, name='login'),
    path('home',views.home),
    path('employee_list',views.employee_list),
    path('add_employee',views.add_employee),
    path('delete_employee',views.delete_employee),
    path('employee_salary',views.employee_salary),
    path('edit_employee/<rid>',views.edit_employee),
    path('edit_employeel/<rid>',views.edit_employeel),
    path('register',views.register),
    path('login',views.e_login),
    path('logout',views.e_logout),
    path('delete/<rid>',views.delete),
    path('activate_employee/<int:rid>/',views.activate_employee),
    path('deactivate_employee/<int:rid>/',views.deactivate_employee),
    path('google-login/', views.google_login),
]
