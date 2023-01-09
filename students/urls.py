from django.urls import path

from students.views import student_list,student_detail,student_api,college_details

urlpatterns = [
    path('student_list/', student_list,name='student_list'),
    path('student_list/<int:pk>/', student_detail,name='student_update'),
    path('student_api/',student_api,name='student_api'),
    path('college_details/',college_details,name='college_details'),
]