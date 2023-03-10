from django.contrib import admin

from src.apps.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "board",
        "lead",
        "start",
        "end",
    )
    list_filter = ("board", "lead", "start", "end")
