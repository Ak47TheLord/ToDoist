from django import forms

from ..models import Project, Task, TaskBoard


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"data_icon": "fa fa-user", "col_cls": "col-md-8"}),
            "description": forms.Textarea(attrs={"data_icon": "fa fa-hashtag", "col_cls": "col-md-12"}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"data_icon": "fa fa-user", "col_cls": "col-md-8"}),
            "description": forms.Textarea(attrs={"data_icon": "fa fa-hashtag", "col_cls": "col-md-12"}),
        }


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['task_board', ]
        widgets = {
            "title": forms.TextInput(attrs={"data_icon": "fa fa-user", "col_cls": "col-md-8"}),

        }


class TaskBoardForm(forms.ModelForm):
    class Meta:
        model = TaskBoard
        fields = "__all__"
        exclude=['project']
        widgets = {
            "title": forms.TextInput(attrs={"data_icon": "fa fa-user", "col_cls": "col-md-8"}),
            "description": forms.Textarea(attrs={"data_icon": "fa fa-hashtag", "col_cls": "col-md-12"}),
        }


class AddTaskBoardForm(forms.ModelForm):
    class Meta:
        model = TaskBoard
        exclude = ['project', ]
        widgets = {
            "title": forms.TextInput(attrs={"data_icon": "fa fa-user", "col_cls": "col-md-8"}),
        }
