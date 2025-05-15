from django.contrib import admin
from .models import Tasks

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    pass

