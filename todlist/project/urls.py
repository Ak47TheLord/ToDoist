from django.urls import path, reverse

from . import views as project_views

urlpatterns = [
    path("", project_views.list_projects, name="list-projects"),
    path("create", project_views.add_project, name="add-projects"),
    path("<int:pk>/view", project_views.view_project, name="view-projects"),
    path("<int:pk>/update", project_views.edit_project, name="update-projects"),
    path("<int:pk>/delete", project_views.delete_project, name="delete-projects"),
    # Task Urls #######
    # path("tasks", project_views.list_tasks, name="list-tasks"),
    path("taskboard/<int:pk>/tasks", project_views.task_board_add_tasks, name="task-board-add-tasks"),
    path("tasks/create", project_views.add_tasks, name="add-tasks"),
    path("tasks/<int:pk>/view", project_views.view_tasks, name="view-tasks"),
    path("tasks/<int:pk>/update", project_views.edit_tasks, name="update-tasks"),
    path("tasks/<int:pk>/delete", project_views.delete_tasks, name="delete-tasks"),

    ###### Task Board  ######

    path("taskboard", project_views.list_task_board, name="list-task-board"),
    path("<int:pk>/taskboard", project_views.project_add_task_board, name="project-add-task-board"),
    path("taskboard/create", project_views.add_task_board, name="add-task-board"),
    path("taskboard/<int:pk>/view", project_views.view_task_board, name="view-task-board"),
    path("taskboard/<int:pk>/update", project_views.edit_task_board, name="update-task-board"),
    path("taskboard/<int:pk>/delete", project_views.delete_task_board, name="delete-task-board"),
]


def list_projects():
    return reverse("list-projects")


def add_projects():
    return reverse("add-projects")


def delete_projects(pk):
    return reverse("delete-projects", kwargs={"pk": pk})


def update_projects(pk):
    return reverse("update-projects", kwargs={"pk": pk})


def view_projects(pk):
    return reverse("view-projects", kwargs={"pk": pk})


#### Task #######

def list_tasks():
    return reverse("list-tasks")


def add_tasks():
    return reverse("add-tasks")


def task_board_add_tasks(pk):
    return reverse("task-board-add-tasks", kwargs={"pk": pk})


def delete_tasks(pk):
    return reverse("delete-tasks", kwargs={"pk": pk})


def update_tasks(pk):
    return reverse("update-tasks", kwargs={"pk": pk})


def view_tasks(pk):
    return reverse("view-tasks", kwargs={"pk": pk})


#### Taskboard #######

def list_task_board():
    return reverse("list-task-board")


def project_add_task_board(pk):
    return reverse("project-add-task-board", kwargs={"pk": pk})


def add_task_board():
    return reverse("add-task-board")


def delete_task_board(pk):
    return reverse("delete-task-board", kwargs={"pk": pk})


def update_task_board(pk):
    return reverse("update-task-board", kwargs={"pk": pk})


def view_task_board(pk):
    return reverse("view-task-board", kwargs={"pk": pk})
