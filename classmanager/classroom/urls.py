from django.urls import path
from classroom import views

app_name = 'classroom'

urlpatterns =[
    path('signup/',views.SignUp,name="signup"),
    path('signup/student_signup/',views.StudentSignUp,name="StudentSignUp"),
    path('signup/teacher_signup/',views.TeacherSignUp,name="TeacherSignUp"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('student/<int:pk>/',views.StudentDetailView.as_view(),name="student_detail"),
    path('teacher/<int:pk>/',views.TeacherDetailView.as_view(),name="teacher_detail"),
    path('update/student/<int:pk>/',views.StudentUpdateView,name="student_update"),
    path('update/teacher/<int:pk>/',views.TeacherUpdateView,name="teacher_update"),
    path('teacher/class_students_list',views.class_students_list,name="class_student_list"),
    path('submit_list/',views.submit_list,name="submit_list"),
    path('change_password/',views.change_password,name="change_password"),
]
