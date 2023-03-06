from django.contrib import admin
from webapp.models import Task, Task_type, Status


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completion_date')
    list_filter = ('id', 'title', 'completion_date')
    search_fields = ('title', 'completion_date')
    fields = ('text', 'title', 'description', 'completion_date')
    readonly_fields = ('id', 'id')


class Task_type_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name', )
    fields = ('name', )
    readonly_fields = ('id', 'id')


class Status_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name', )
    fields = ('name', )
    readonly_fields = ('id', 'id')


admin.site.register(Task, TaskAdmin)
admin.site.register(Task_type, Task_type_Admin)
admin.site.register(Status, Status_Admin)
