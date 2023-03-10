from django.contrib import admin

from src.apps.boards.models import Board, Label


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "description", "owner")
    list_filter = ("owner",)
    raw_id_fields = ("statuses",)
    search_fields = ("slug",)


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "color", "board")
    list_filter = ("board",)
