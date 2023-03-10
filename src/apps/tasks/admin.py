from django.contrib import admin

from src.apps.tasks.models import TaskStatus, Task


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "type")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "reference_id",
        "title",
        "description",
        "board",
        "project",
        "status",
        "assignee",
        "pull_requests",
    )
    list_filter = ("board", "project", "status", "assignee")
    raw_id_fields = ("children", "related_tasks", "reviewers", "labels")
