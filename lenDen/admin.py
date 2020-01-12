from django.contrib import admin
from .models import Students, Classrooms, Teachers, Subjects, Schools

# Register your models here.


@admin.register(Classrooms)
class ClassroomsAdmin(admin.ModelAdmin):
	a = 10

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
	b = 100

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
	
	def __str__(self):
		return 'Subject: {}'.format(self.name)

@admin.register(Schools)
class SchoolsAdmin(admin.ModelAdmin):
	d = 300

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    e = 400