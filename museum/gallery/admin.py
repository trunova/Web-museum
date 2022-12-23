from django.contrib import admin
from gallery.models import *
from django.contrib.auth.models import Group, User

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_and_time', 'description']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'post', 'email']

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ['hall_number', 'title']

@admin.register(Museum_piece)
class Museum_pieceAdmin(admin.ModelAdmin):
    list_display = ['piece_name', 'description', 'date_of_creation', 'piece_type', 'author_id', 'hall_id']

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'email']

@admin.register(Exhibition_employee)
class Exhibition_employeeAdmin(admin.ModelAdmin):
    list_display = ['exhibition_id', 'employee_id']

@admin.register(Exhibition_museum_piece)
class Exhibition_museum_pieceAdmin(admin.ModelAdmin):
    list_display = ['exhibition_id', 'museum_piece_id']

@admin.register(Exhibition_visitor)
class Exhibition_visitorAdmin(admin.ModelAdmin):
    list_display = ['exhibition_id', 'visitor_id']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email']

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['piece']