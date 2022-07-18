from django.contrib import admin
from . import models as task_models

# Register your models here.

admin.site.register(task_models.Project)
admin.site.register(task_models.TaskBoard)
admin.site.register(task_models.Task)
