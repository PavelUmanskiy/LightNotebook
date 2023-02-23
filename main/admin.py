from django.contrib import admin

from .models import *


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'date_open',
        'deadline',
        'date_done',
        'is_closed',
        'budget',
        'expenses',
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = (
        'title',
        'description',
        'date_open',
        'deadline',
        'date_done',
        'is_closed',
        'budget',
        'expenses',        
    )
    list_filter = (
        'date_open',
        'deadline',
        'date_done',
        'is_closed',
    )
    
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'date_open',
        'deadline',
        'date_done',
        'is_done',
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = (
        'id',
        'title',
        'description',
        'date_open',
        'deadline',
        'date_done',
        'is_done',
    )
    list_filter = (
        'date_open',
        'deadline',
        'date_done',
        'is_done',
    )


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number')
    list_display_links = ('id', 'user')
    search_fields = ('id', 'user', 'phone_number')
    list_editable = ('phone_number',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'address',
        'email',
        'phone_number',
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'email', 'phone_number')
    list_editable = (
        'name',
        'description',
        'address',
        'email',
        'phone_number',
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'team_leader',
    )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_editable = ('name', 'description')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'email',
        'phone_number',
        'payment_status',
    )
    list_display_links = ('id', 'name')
    search_fields = (
        'name',
        'description',
        'email',
        'phone_number',
        'payment_status',
    )
    list_filter = ('payment_status')
    list_editable = (
        'name',
        'description',
        'email',
        'phone_number',
        'payment_status'
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime_added', 'user', 'content')
    list_display_links = ('id')
    search_fields = ('datetime_added', 'user', 'content')
    list_editable = ('content',)
    list_filter = ('user', 'datetime_added')
