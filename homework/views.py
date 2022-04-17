from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from homework.models import Student, Person, Group, Subject, Course, Lesson


def index(request):
    return HttpResponse('Hello World!')

def home(request):
    container = 'Hello World!'
    return render(request, 'home.html', context={
        'container': container,
    })

def students_json(request):
    students = Student.objects.all()
    return JsonResponse({'students': list(students)})



def person_add(request):
    new_person = Person()
    new_person.first_name = 'Christopher'
    new_person.last_name = 'Chapman'
    new_person.type_person = 'Mage'
    new_person.save()
    return HttpResponse('Added')


def person_list(request):
    person = Person.objects.all().values()
    return JsonResponse({'person': list(person)})


def person_delete(request):

    try:
        delete_person = Person.objects.get(first_name='Christopher')
    except (Person.MultipleObjectsReturned):
        delete_person = Person.objects.filter(first_name='Christopher')[0]
    except Person.DoesNotExist:
        delete_person = None
    if delete_person is None:
        return HttpResponse('Not exist')
    else:
        delete_person.delete()
    return HttpResponse('Deleted')


def person_update(request):
    update_person = Person.objects.get(first_name='Christopher')
    update_person.last_name = 'Chap'
    update_person.save()

    return HttpResponse('Updated')


def group_add(request):
    new_group = Group()
    new_group.group_name = 'PythonPro'
    new_group.group_city = 'Odessa'
    new_group.save()

    return HttpResponse('Added')


def group_list(request):
    group = Group.objects.all().values()
    return JsonResponse({'group': list(group)})


def group_delete(request):

    try:
        delete_group = Group.objects.get(group_name='PythonPro')
    except (Group.MultipleObjectsReturned):
        delete_group = Group.objects.filter(group_name='PythonPro')[0]
    except Group.DoesNotExist:
        delete_group = None

    if delete_group is None:
        return HttpResponse('Not exist')
    else:
        delete_group.delete()

    return HttpResponse('Deleted')


def group_update(request):
    update_group = Group.objects.get(group_name='PythonPro')
    update_group.group_city = 'Lviv'
    update_group.save()
    return HttpResponse('Updated')


def subject_add(request):
    new_subject = Subject()
    new_subject.subject_name = 'Python'
    new_subject.save()

    return HttpResponse('Added')


def subject_list(request):
    subject = Subject.objects.all().values()
    return JsonResponse({'subject': list(subject)})


def subject_delete(request):

    try:
        delete_subject = Subject.objects.get(subject_name='Python')
    except (Subject.MultipleObjectsReturned):
        delete_subject = Subject.objects.filter(subject_name='Python')[0]
    except Subject.DoesNotExist:
        delete_subject = None

    if delete_subject is None:
        return HttpResponse('Not exist')
    else:
        delete_subject.delete()

    return HttpResponse('Deleted')


def subject_update(request):
    update_subject = Subject.objects.get(subject_name='Python')
    update_subject.subject_level = 'Hard'
    update_subject.save()
    return HttpResponse('Updated')


def course_add(request):
    new_course = Course()
    new_course.course_name = 'Python'
    new_course.save()
    return HttpResponse('Added')


def course_list(request):
    course = Course.objects.all().values()
    return JsonResponse({'course': list(course)})


def course_delete(request):

    try:
        delete_course = Course.objects.get(course_name='Python')
    except (Course.MultipleObjectsReturned):
        delete_course = Subject.objects.filter(course_name='Python')[0]
    except Course.DoesNotExist:
        delete_course = None

    if delete_course is None:
        return HttpResponse('Not exist')
    else:
        delete_course.delete()

    return HttpResponse('Deleted')


def course_update(request):
    update_course = Course.objects.get(course_name='Python')
    update_course.course_type = 'Programming'
    update_course.save()
    return HttpResponse('Updated')


def lesson_add(request):
    new_lesson = Lesson()
    new_lesson.lesson_name = 'Python'
    new_lesson.save()
    return HttpResponse('Added')


def lesson_list(request):
    lesson = Lesson.objects.all().values()
    return JsonResponse({'lesson': list(lesson)})


def lesson_delete(request):

    try:
        delete_lesson = Lesson.objects.get(lesson_name='Python')
    except (Lesson.MultipleObjectsReturned):
        delete_lesson = Lesson.objects.filter(lesson_name='Python')[0]
    except Lesson.DoesNotExist:
        delete_lesson = None

    if delete_lesson is None:
        return HttpResponse('Not exist')
    else:
        delete_lesson.delete()

    return HttpResponse('Deleted')


def lesson_update(request):
    update_lesson = Lesson.objects.get(lesson_name='Python')
    update_lesson.lesson_type = 'Django'
    update_lesson.save()
    return HttpResponse('Updated')


def index_with_get(request):
    name = request.GET.get('name')
    if not name:
        name = 'stranger'
    return HttpResponse(f'Hello, {name}')
