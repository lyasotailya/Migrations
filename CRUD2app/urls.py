from django.urls import path

from CRUD2app.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
]
