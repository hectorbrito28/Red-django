from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model

from django.contrib import messages

from .forms import UserFormsignup


from django.contrib.auth import login,authenticate,logout


from django.db import IntegrityError


from django.contrib.auth.hashers import check_password

from django.contrib.auth.decorators import login_required

from .forms import TaskForm,Taskform2

from .models import Task


from datetime import datetime

# Create your views here.


def signupview(request):
    if request.method == "GET":
        return render(
            request, template_name="signup.html", context={"userform": UserFormsignup}
        )

    else:
        user = get_user_model()

        username = request.POST["username"]
        password1 = request.POST["password1"]

        if request.POST["password1"] == request.POST["password2"]:
            try:
                uservar = user.objects.create_user(
                    username=username, password=password1
                )

                uservar.save()
                
                user_authenticated = authenticate(request,username=username,password=password1)
                
                if user_authenticated is not None:
                
                    login(request,user_authenticated)
                    messages.success(request, "Tu cuenta ha sido creada")
                    messages.success(request, "Te has logueado exitosamente")
                    return redirect("Home")
                    
            except IntegrityError:
                messages.error(request, "Ese usuario ya existe")

        else:
            messages.error(request, "La contraseña no coincide")

        return redirect("signup")


def home(request):
    return render(request,template_name="home.html")

@login_required
def logoutview(request):
    logout(request)
    messages.success(request,"Se ha cerrado sesion")
    return redirect("Home")


def signin(request):
    if request.method == "GET":
        return render(request,template_name="signin.html",context={"form":AuthenticationForm})
    
    else:
        username = request.POST["username"]
        password1 = request.POST["password"]
        #password2 = request.POST["password2"]
        
        usermodel = get_user_model()
        
        
        try:
            result = usermodel.objects.get(username=username)
        
            

            if check_password(password1,result.password):
            
                userauth = authenticate(request,username=username,password=password1)
                
                login(request,userauth)
                messages.success(request,"Te has logueado correctamente")
                
            else:
                messages.error(request,"La contraseña no coincide")
        except:
            messages.error(request,"Usuario no existe")
            
        return redirect("Home")
    
    

@login_required
def taskview(request):
    
    
    if request.method == "GET":
        
    
    
        tasks = Task.objects.filter(user_id=request.user.id)
    
        return render(request,template_name="tasks.html",context={"form":TaskForm,"tasks":tasks})   
    
    else:
        
        name = request.POST["name"]
        description = request.POST["description"]
        
        try:
        
            #Task.objects.create(name=name,description=description,user_id=request.user.id)# Tambien se puede asi
            
            task = Taskform2(request.POST)
            
            newtask = task.save(commit=False)
            
            newtask.user = request.user
            
            
            print(task)
            
            task.save()
        
        except:
            messages.error(request,"Por favor escribe algun dato valido")
        
        return redirect("TASK")
    



@login_required
def deletetask(request):
    taskid = request.POST["task"]
    
    Task.objects.get(id=taskid).delete()
    
    return redirect("TASK")
    


@login_required
def savetask(request):
    if request.method == "GET":
        return redirect("TASK")
    
    else:
    
        try:
                
            task = Task.objects.get(id=request.POST["task"])
                
            task.completed = True
                
            task.save()
            
        except:
            messages.error(request,"Ha ocurrido un error")
        
        
        return redirect("TASK")
    
    
    


@login_required
def taskdetail(request):
    
    if request.method == "GET":
    
        taksid= request.GET["taskdetail"]
        
        task = get_object_or_404(Task,pk=taksid)
        
        #Se puede colocar tambien la task en initial
        
        form = Taskform2(instance=task)
        
        return render(request,template_name="task_detail.html",context={"task":task,"form":form})
    
    else:
        
        print(request.POST)
        
        task = Task.objects.get(id=request.POST["task"])
        form = Taskform2(request.POST,instance=task)
        form.save()
        
        #task.name = request.POST["name"]
        
        #task.description = request.POST["description"]
        
        #task.save()

        return redirect("TASK")
    