import django_tables2 as tables
from django.utils.html import format_html

from ..models import Project, Task, TaskBoard


class ProjectTable(tables.Table):
    actions = tables.Column(empty_values=())

    class Meta:
        attrs = {"class": "table data-table"}
        model = Project
        fields = ["id", "title", "created_at", "actions"]

    def render_id(self, value):
        return "#{}".format(value)

    def render_actions(self, record):
        return format_html("""
        <a class="btn btn-sm btn-outline-info" href="%s">Edit</a>
        <a onclick="show_swal(this)" data-url="%s" data-title="%s" class="btn btn-sm btn-outline-danger" href="%s">Delete</a>
        <a class="btn btn-sm btn-secondary" href="%s">View</a>

        """ % (record.edit_url(), record.delete_url, record.title, "javascript:;", record.view_url()))


class TaskTable(tables.Table):
    actions = tables.Column(empty_values=())

    class Meta:
        attrs = {"class": "table data-table"}
        model = Task
        fields = ["id", "title", "created_at", "actions"]

    def render_id(self, value):
        return "#{}".format(value)

    def render_actions(self, record):
        return format_html("""
        <a class="btn btn-sm btn-outline-info" href="%s">Edit</a>
        <a onclick="show_swal(this)" data-url="%s" data-title="%s" class="btn btn-sm btn-outline-danger" href="%s">Delete</a>
        <a class="btn btn-sm btn-secondary" href="%s">View</a>

        """ % (record.edit_url(), record.delete_url, record.title, "javascript:;", record.view_url()))


class TaskBoardTable(tables.Table):
    actions = tables.Column(empty_values=())

    class Meta:
        attrs = {"class": "table data-table"}
        model = TaskBoard
        fields = ["id", "title", "created_at", "actions"]

    def render_id(self, value):
        return "#{}".format(value)

    def render_actions(self, record):
        return format_html("""
        <a class="btn btn-sm btn-outline-info" href="%s">Edit</a>
        <a onclick="show_swal(this)" data-url="%s" data-title="%s" class="btn btn-sm btn-outline-danger" href="%s">Delete</a>
        <a class="btn btn-sm btn-secondary" href="%s">View</a>

        """ % (record.edit_url(), record.delete_url(), record.title, "javascript:;", record.view_url()))
