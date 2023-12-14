from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Employee
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    employees = Employee.objects.filter(is_active=True)
    total_count = employees.count()  
    total_salary = employees.aggregate(total_salary=Sum('salary'))['total_salary'] or 0  
    context = {'total_count': total_count, 'total_salary': total_salary}
    return render(request, 'index.html', context)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def employee_list(request):
    employees = Employee.objects.all()
    
    paginator = Paginator(employees, 10)
    
    page = request.GET.get('page')
    
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    context = {'data': data}
    
    return render(request, 'employee_list.html', context)


def edit_employeel(request,rid):
    if request.method=='POST':
        n=request.POST['name']
        j=request.POST['joinDate']
        b=request.POST['birthDate']
        e=request.POST['email']
        m=request.POST['mobile']
        s=request.POST['salary']
        u=Employee.objects.filter(id=rid)
        u.update(name=n,joinDate=j,birthDate=b,email=e,mobile=m,salary=s)
        return redirect('/employee_list')       
    else:
        m=Employee.objects.get(id=rid)
        context={}
        context['data']=m 
        return render(request,'edit_employee.html',context)

def add_employee(request):
    if request.method=='POST':
        n=request.POST['name']
        j=request.POST['joinDate']
        b=request.POST['birthDate']
        e=request.POST['email']
        m=request.POST['mobile']
        s=request.POST['salary']
        context={}
        if n=="" or j=="" or b=="" or e=="" or m=="" or s=="":
            context['errmsg']="fields can not be empty"
            return render(request,'add_employee.html',context)
        else:
            try:
                e=Employee.objects.create(name=n,joinDate=j,birthDate=b,email=e,mobile=m,salary=s)
                e.save()
                context['suc']="Employee Added Successfully"
                return render(request,'add_employee.html',context)
            except Exception:
                context['errmsg']="Error Adding Employee"
                return render(request,'add_employee.html',context)
    else:
        return render(request,'add_employee.html')

def delete_employee(request):
    m=Employee.objects.all()
    paginator = Paginator(m, 10)
    
    page = request.GET.get('page')
    
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    context = {'data': data}
    return render(request,'delete_employee.html',context)

def delete(request,rid):
    #print("id to be delete:",rid)
    m=Employee.objects.filter(id=rid)
    m.delete()
    return redirect('/delete_employee')

def employee_salary(request):
    m=Employee.objects.all()
    paginator = Paginator(m, 10)
    
    page = request.GET.get('page')
    
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    context = {'data': data}
    return render(request,'employee_salary.html',context)

def edit_employee(request,rid):
    if request.method=='POST':
        n=request.POST['name']
        j=request.POST['joinDate']
        b=request.POST['birthDate']
        e=request.POST['email']
        m=request.POST['mobile']
        s=request.POST['salary']
        u=Employee.objects.filter(id=rid)
        u.update(name=n,joinDate=j,birthDate=b,email=e,mobile=m,salary=s)
        return redirect('/employee_salary')       
    else:
        m=Employee.objects.get(id=rid)
        context={}
        context['data']=m 
        context['edit'] = 1
        return render(request,'edit_employee.html',context)

def register(request):
    if request.method=='POST':
        n=request.POST['username']
        p=request.POST['password']
        cp=request.POST['cpassword']
        context={}
        if n=="" or p=="" or cp=="":
            context['errmsg']="fields can not be empty"
            return render(request,'register.html',context)
        elif p != cp:
            context['errmsg']="Password Did not match"
            return render(request,'register.html',context)
        else:
            try:
                u=User.objects.create(username=n,email=n,password=p)
                u.set_password(p)
                u.save()
                context['suc']="User Created sucessfully please Login"
                return render(request,'register.html',context)
            except Exception:
                context['errmsg']="UserName exist already try another"
                return render(request,'register.html',context)
    else:
        return render(request,'register.html') 

def e_logout(request):
    logout(request)
    return redirect('/login')

def e_login(request):
    if request.method=='POST':
        n=request.POST['username']
        p=request.POST['password']
        context={}
        if n=="" or p=="":
            context['errmsg']="fields can not be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=n,password=p)
            if u is not None:
                login(request,u)
                return redirect('/home')
            else:
                context['errmsg']="Invalid Username and password"
                return render(request,'login.html',context)
    else:
        return render(request,'login.html')
    
def activate_employee(request, rid):
    try:
        employee = Employee.objects.get(id=rid)
        employee.is_active = True
        employee.save()
    except Employee.DoesNotExist:
        pass
    return redirect('/employee_list')

def deactivate_employee(request, rid):
    try:
        employee = Employee.objects.get(id=rid)
        employee.is_active = False
        employee.save()
    except Employee.DoesNotExist:
        pass
    return redirect('/employee_list')


from django.http import JsonResponse

def google_login(request):
    if request.method == 'POST':
        google_email = request.POST.get('google_email')
        if google_email:
            context = {}
            # Check if the Google email exists in your User database
            user = User.objects.filter(email=google_email).first()

            if user:
                # If the user exists, log them in and redirect to the home page
                login(request, user)
                return redirect('/home')
            else:
                # If the user doesn't exist, create an account and log them in
                # You can generate a random password here or let the user set one
                password = User.objects.make_random_password()
                user = User.objects.create(username=google_email, email=google_email, password=password)
                user.set_password(password)
                user.save()
                login(request, user)
                return redirect('/home')
        else:
            # Handle the case where the Google email is missing in the request
            return JsonResponse({'message': 'Google email is missing in the request'}, status=400)
    else:
        # Handle invalid request method
        return JsonResponse({'message': 'Invalid request method'}, status=400)