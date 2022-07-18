from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from ..models import Project, Task, TaskBoard
from . import tables as project_table
from . import urls as project_urls
from . import forms as project_forms
from . import utils as project_utils


def list_projects(request):
    queryset = Project.objects.all()
    table = project_table.ProjectTable(queryset)
    context = {
        "title": "List Projects",
        "table": table,
        "actions": [
            {
                "title": "Add Project",
                "href": project_urls.add_projects(),
                "classes": "btn btn-success",
                "icon": "fa fa-plus"
            },
            {
                "title": "Refresh",
                "href": project_urls.list_projects(),
                "classes": "btn btn-primary",
                "icon": "fa fa-sync"
            }
        ],
        "active_pcls": "active",
    }
    return render(request, "Project/tables.html", context)


def add_project(request):
    form = project_forms.ProjectForm(request.POST or None)
    if request.method == "POST":
        obj = form.save()
        project_utils.get_task_board(obj)
        message = f'Project: {obj.title}! You have been Added!'
        messages.success(request, message)
        return redirect(project_urls.list_projects())
    context = project_utils.get_project_context(form, project_urls.add_projects(), project_urls.list_projects(),
                                                "Add Project")
    context['active_pcls'] = "active"
    return render(request, "Project/add-update.html", context)


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = project_forms.ProjectForm(request.POST or None, instance=project)
    if request.method == "POST":
        form.save()
        message = f'Project: {project.title}! You have been Edited!'
        messages.success(request, message)
        return redirect(project_urls.list_projects())
    context = project_utils.get_project_context(form, project_urls.update_projects(pk), project_urls.list_projects(),
                                                "Edit {}".format(project.title))
    context['active_pcls'] = "active"
    return render(request, "Project/add-update.html", context)


def view_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    task_board = TaskBoard.objects.filter(project=project)
    table = project_table.TaskBoardTable(task_board)
    form = project_forms.ProjectForm(request.POST or None, instance=project)
    if request.method == "POST":
        form.save()
        message = f'Project: {project.title}! Task Board have been settled!'
        messages.success(request, message)
        return redirect(project_urls.list_projects())
    context = project_utils.get_project_context(form, project_urls.view_projects(pk), project_urls.list_projects(),
                                                "View {}".format(project.title))
    context['read_only'] = True
    context["entry"] = True
    context["table"] = table
    context["pk"] = pk
    context['active_pcls'] = "active"

    return render(request, "Project/add-update.html", context)


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return JsonResponse({
        "success": True,
        "message": f'Project: {project.title}! have been deleted!'
    }, safe=False)


####### Task Board #########


def list_task_board(request):
    queryset = TaskBoard.objects.all()
    table = project_table.TaskBoardTable(queryset)
    context = {
        "title": "List Tasks Board",
        "table": table,
        "actions": [
            {
                "title": "Add Task Board",
                "href": project_urls.add_task_board(),
                "classes": "btn btn-success",
                "icon": "fa fa-plus"
            },
            {
                "title": "Refresh",
                "href": project_urls.list_task_board(),
                "classes": "btn btn-primary",
                "icon": "fa fa-sync"
            }
        ],
        "active_tcls": "active",
    }
    return render(request, "Project/tables.html", context)


def project_add_task_board(request, pk):
    form = project_forms.AddTaskBoardForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            project = Project.objects.get(pk=pk)
            obj = form.save(commit=False)
            obj.project = project
            obj.save()
            message = f'Task Board: {obj.title}!  have been Created!'
            messages.success(request, message=message)
            return redirect(project_urls.view_projects(pk))
    context = project_utils.get_project_context(form, project_urls.project_add_task_board(pk),
                                                project_urls.view_projects(pk),
                                                "Add Task Board")
    context['active_pcls'] = "active"
    return render(request, "Project/add-update.html", context)


def add_task_board(request):
    form = project_forms.TaskBoardForm(request.POST or None)
    if request.method == "POST":
        form.save()
        return redirect(project_urls.list_task_board())
    context = project_utils.get_project_context(form, project_urls.add_task_board(), project_urls.list_task_board(),
                                                "Add Task Board")
    context["AddTask"] = {
        'btn_class': 'btn btn-primary',
        'add_class': 'fa fa-plus',
        'name': "Add Task",
        'href': reverse('add-tasks')
    }
    context['active_pcls'] = "active"
    return render(request, "Project/add-update.html", context)


def edit_task_board(request, pk):
    task_board = get_object_or_404(TaskBoard, pk=pk)
    # project = Project.objects.get()
    form = project_forms.TaskBoardForm(request.POST or None, instance=task_board)
    if request.method == "POST":
        form.save()
        message = f'Task Board: {task_board.title}!  have been Edited!'
        messages.success(request, message=message)
        return redirect(project_urls.view_projects(task_board.project.pk))
    context = project_utils.get_project_context(form, project_urls.update_task_board(pk),
                                                project_urls.view_projects(task_board.project.pk),
                                                "Edit {}".format(task_board.title))
    # project_urls.list_task_board(),
    context['active_pcls'] = "active"
    return render(request, "Project/add-update.html", context)


def view_task_board(request, pk):
    task_board = get_object_or_404(TaskBoard, pk=pk)
    tasks = Task.objects.filter(task_board=task_board)

    form = project_forms.TaskBoardForm(request.POST or None, instance=task_board)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return reverse(project_urls.view_projects(task_board.project.pk))
        else:
            print("these are the errors", form.errors)
    context = project_utils.get_project_context(form, project_urls.update_task_board(pk),
                                                project_urls.view_projects(task_board.project.pk),
                                                "Edit {}".format(task_board.title))
    table = project_table.TaskTable(tasks)
    context["entry"] = True
    context["table"] = table
    context['read_only'] = True
    context["AddTask"] = {
        'btn_class': 'btn btn-primary',
        'add_class': 'fa fa-plus',
        'name': "Add Task",
        'href': project_urls.task_board_add_tasks(pk),
        # 'href': reverse(project_urls.task_board_add_tasks(pk))
    }
    context['active_pcls'] = "active"
    return render(request, "Project/add-update.html", context)


def delete_task_board(request, pk):
    task_board = get_object_or_404(TaskBoard, pk=pk)
    task_board.delete()
    return JsonResponse({
        "success": True,
        "message": "TaskBoard deleted!"
    }, safe=False)


##### Task Handling ###########


# def list_tasks(request):
#     queryset = Task.objects.all()
#     table = project_table.TaskTable(queryset)
#     context = {
#         "title": "List Tasks",
#         "table": table,
#         "entry": True,
#         "actions": [
#             {
#                 "title": "Add Task",
#                 "href": project_urls.add_tasks(),
#                 "classes": "btn btn-success",
#                 "icon": "fa fa-plus"
#             },
#             {
#                 "title": "Refresh",
#                 "href": project_urls.list_tasks(),
#                 "classes": "btn btn-primary",
#                 "icon": "fa fa-sync"
#             }
#         ]
#     }
#     return render(request, "Project/add-update.html", context)


def add_tasks(request):
    form = project_forms.TaskForm(request.POST or None)
    if request.method == "POST":
        form.save()
        return redirect(project_urls.list_tasks())
    context = project_utils.get_project_context(form, project_urls.add_tasks(), project_urls.list_tasks(),
                                                "Add Task")
    context['active_tcls'] = "active"

    return render(request, "Project/add-update.html", context)


def task_board_add_tasks(request, pk):
    task_board = get_object_or_404(TaskBoard, pk=pk)
    form = project_forms.AddTaskForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            obj: Task
            obj.task_board = task_board
            obj.save()
            message = f'Task: {obj.title}! of Task Board:{task_board.title} have been Created!'
            messages.success(request, message=message)
            return redirect(project_urls.task_board_add_tasks(pk))

    task = Task.objects.filter(task_board=task_board)
    table = project_table.TaskTable(task)
    context = project_utils.get_project_context(form, project_urls.task_board_add_tasks(pk),
                                                project_urls.view_task_board(pk),
                                                "Add Task")
    context["entry"] = True
    context["table"] = table
    context['active_pcls'] = "active"
    # context["pk"] = pk
    return render(request, "Project/add-update.html", context)


def edit_tasks(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = project_forms.AddTaskForm(request.POST or None, instance=task)
    if request.method == "POST":
        form.save()
        message = f'Task: {task.title}! of Task Board:{task.task_board.title} have been Edited!'
        messages.success(request, message=message)
        return redirect(project_urls.view_task_board(task.task_board.pk))
    context = project_utils.get_project_context(form, project_urls.update_tasks(pk),
                                                project_urls.view_task_board(task.task_board.pk),
                                                "Edit {}".format(task.title))
    context['active_pcls'] = "active"
    return render(request, "Project/add-update.html", context)


def view_tasks(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = project_forms.AddTaskForm(request.POST or None, instance=task)
    if request.method == "POST":
        form.save()
        return redirect(project_urls.list_projects())
    context = project_utils.get_project_context(form, project_urls.update_tasks(pk),
                                                project_urls.task_board_add_tasks(task.task_board.pk),
                                                "View {}".format(task.title))

    context['read_only'] = True
    context['active_pcls'] = "active"
    print(context)
    return render(request, "Project/add-update.html", context)


def delete_tasks(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return JsonResponse({
        "success": True,
        "message": "Task deleted!"
    }, safe=False)
