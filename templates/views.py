from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def employee_list(request):
    return render(request,'employee_list.html')

def add_employee(request):
    return render(request,'add_employee.html')

def delete_employee(request):
    return render(request,'delete_employee.html')

def employee_salary(request):
    return render(request,'employee_salary.html')

