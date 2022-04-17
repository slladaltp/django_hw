"""hillel_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homework.views import index, index_with_get, students_json, \
    person_add, person_list, person_delete, person_update, group_add, \
    group_list, group_delete, group_update, subject_add, subject_list, subject_delete, \
    subject_update, course_add, course_list, course_delete, course_update, lesson_add, \
    lesson_list, lesson_delete, lesson_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students_page/', index_with_get),
    path('students_json/', students_json),
    path('add/person', person_add),
    path('list/person', person_list),
    path('delete/person', person_delete),
    path('update/person', person_update),
    path('add/group', group_add),
    path('list/group', group_list),
    path('delete/group', group_delete),
    path('update/group', group_update),
    path('add/subject', subject_add),
    path('list/subject', subject_list),
    path('delete/subject', subject_delete),
    path('update/subject', subject_update),
    path('add/course', course_add),
    path('list/course', course_list),
    path('delete/course', course_delete),
    path('update/course', course_update),
    path('add/lesson', lesson_add),
    path('list/lesson', lesson_list),
    path('delete/lesson', lesson_delete),
    path('update/lesson', lesson_update)
]