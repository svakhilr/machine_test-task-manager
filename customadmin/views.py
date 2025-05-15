from django.shortcuts import render,redirect
from tasks.models import Tasks
from users.models import CustomUser
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        print("user",user)
        if user:
            print("success")
            if user.role == CustomUser.SUPER_ADMIN:
                login(request,user)
                return redirect('get-users')
            elif user.role == CustomUser.ADMIN:
                login(request,user)
                return redirect('tasks')
            else:
                return redirect('admin-login')


    return render(request,"signin.html")



@login_required
def get_users(request):
    users = CustomUser.objects.exclude(role = CustomUser.SUPER_ADMIN)
    context = {
        "users":users
    }
    return render(request,"users.html",context)

def delete_user(request,**kwargs):
    user_id = kwargs.get('user_id')
    CustomUser.objects.get(id=user_id).delete()
    return redirect('get-users')


@login_required
def get_tasks(request):
    tasks = Tasks.objects.all().order_by('-id')
    context = {
        "tasks":tasks
    }
    return render(request,"tasks.html",context)

@login_required
def get_task_detail(request,**kwargs):
    task_id = kwargs.get("task_id")
    task = Tasks.objects.get(id=task_id)
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        task_status = request.POST.get("task_status")
        assigned_to = request.POST.get("assigned_to")
        description = request.POST.get("discription")
        worked_hours = request.POST.get("worked_hours")
        
        task.title = title
        task.task_status = task_status
        task.description = description

        if worked_hours is None:
            task.worked_hours = 0
        else:
            task.worked_hours = worked_hours

        if assigned_to.isdigit():
            user = CustomUser.objects.get(id=assigned_to)
            print("user",user)
            task.assigned_to = user
        task.save()
        return redirect("tasks")

    users = CustomUser.objects.filter(role=CustomUser.USER)
    context = {
        "task":task,
        "users":users
    }
    print(task_id)
    return render(request,"taskedit.html",context)

@login_required
def add_task(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")
        due_date = data.get("due_date")
        Tasks.objects.create(title=title,description=description,due_date=due_date)
        return redirect('tasks')
    return render(request,"addtask.html")


