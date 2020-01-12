from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Count
from .models import Classrooms, Subjects, Teachers, Students, Schools

# Create your views here.


class ClassroomView(TemplateView):
    
    # paginate_by = 20
    # model = Classrooms
    template_name = "lentemplates/classroomtable.html"

    def get_context_data(self, **kwargs):
        ctx = super(ClassroomView, self).get_context_data(**kwargs)
        tabular_content = []
        if self.kwargs.get('id'):
            school = Schools.objects.select_related(
                'teacher', 'classroom').filter(id=int(self.kwargs.get('id')))
            if school and school.first().subjects and school.first().teacher:
                school_all_subject_ids = []
                school_all_teacher_ids = []
                for school_sub in school.first().subjects:
                    school_all_subject_ids.append(school_sub.id)
                for school_teacher in school.first().teacher:
                    school_all_teacher_ids.append(school_teacher.id)
                for classroom in school.first().classroom:
                    if classroom.subject:
                        classroom_subjects_name = []
                        for class_sub in classroom.subject:
                            class_sub_teachers = class_sub.teachers_set.all()
                            class_sub_teachers_name = []
                            for teacher in class_sub_teachers:
                                if teacher.id in school_all_teacher_ids:
                                    class_sub_teachers_name.append(teacher.name)
                            if class_sub.id in school_all_subject_ids:
                                for cstn in class_sub_teachers_name:
                                    tabular_content.append({
                                        'id': classroom.id, 
                                        'classroom_name': classroom.name,
                                        'classroom_subject': class_sub.name,
                                        'classroom_subject_teacher': cstn})
        ctx['tabular_content']=tabular_content
        return ctx

    def get(self, request, *args, **kwargs):
        ctx = self.get_context_data(**kwargs)
        return render(request, self.template_name, ctx)

class ProblemStatement2(TemplateView):

    template_name = "lentemplates/problem_statement2.html"


def problem_statement3(request):
    teacher_content = []
    teachers_salary = Teachers.objects.prefetch_related('student_associated').filter(salary__gte=100000)
    if teachers_salary:
        for teacher in teachers_salary:
            teacher_content.append({
                'teacher_id': teacher.id,
                'student_count': teacher.student_associated_set.count(),
                'teacher_name': teacher.name,
                'teachers_salary': teacher.salary})
    ctx = {'teacher_content': teacher_content}
    return render(request, "lentemplates/problem_statement3.html", ctx)

def problem_statement4(request):
    ctx = {}
    all_subjects = Subjects.objects.annotate(
        teachers_subjects_count=Count('teachers__subjects'), subject_student_count=Count('teachers__student_associated')).filter(
        teachers_subjects_count__gt=1).values_list(
        'name', 'subject_student_count', 'teachers_subjects_count', 'total_durations')
    ctx['all_subjects'] = all_subjects if all_subjects else None
    return render(request, "lentemplates/problem_statement4.html", ctx)