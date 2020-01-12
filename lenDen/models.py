from django.db import models

# Create your models here.


class Students(models.Model):
	name = models.CharField(blank=True, null=True, max_length=400)
	DOJ = models.DateField(auto_now=True)
	standard = models.CharField(blank=True, null=True, max_length=5)
	roll_no = models.SmallIntegerField(null=True, blank=True)
	ranking = models.IntegerField(null=True, blank=True)
	point_of_contact = models.CharField(blank=True, null=True, max_length=1000)

	class Meta:
		db_table = 'students'


class Subjects(models.Model):
	name = models.CharField(blank=True, null=True, max_length=40)
	Chapters = models.CharField(blank=True, null=True, max_length=400)
	total_durations = models.DurationField(blank=True, null=True)	
	per_class_duration = models.DurationField(blank=True, null=True)

	class Meta:
		db_table = 'subjects'
 
class Classrooms(models.Model):

	SHAPE_CHOICES = (
		(1, 'oval'),
		(2, 'rectangular'),
		(3, 'canopy'),
		(4, 'elevated')
	)
	name = models.CharField(blank=True, null=True, max_length=400)
	seating_capacity = models.SmallIntegerField(default=0)
	web_lecture_support = models.BooleanField(default=False)
	shape = models.PositiveSmallIntegerField(
		choices=SHAPE_CHOICES, default=SHAPE_CHOICES[1])
	subject = models.ManyToManyField(Subjects, blank=True)

	class Meta:
		db_table = 'classrooms'


class Teachers(models.Model):
	name = models.CharField(blank=True, null=True, max_length=400)
	DOJ  = models.DateField(auto_now=True)
	subjects = models.ManyToManyField(Subjects, blank=True)
	salary = models.IntegerField(default=0)
	student_associated = models.ManyToManyField(Students, blank=True)

	class Meta:
		db_table = 'teachers'


class Schools(models.Model):
	teacher = models.ForeignKey(Teachers, blank=True, null=True)
	students = models.ForeignKey(Students, blank=True, null=True)
	classroom = models.ForeignKey(Classrooms, blank=True, null=True)
	subjects = models.ManyToManyField(Subjects, blank=True)

	class Meta:
		db_table = 'schools'
