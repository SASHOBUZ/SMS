from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('students/', views.Students, name='students'),
    path('teachers/', views.Teachers, name='teachers'),
    path('accounts/', views.Account, name='accounts'),
    path('add_student/', views.CreateStudent, name='add_student'),
    path('add_teacher/', views.CreateTeacher, name='add_teacher'),
    path('add_fees/', views.AddFees, name='add_fees'),
    path('update_student/<str:pk>/', views.UpdateStudent, name='update_student'),
    path('delete_student/<str:pk>/', views.DeleteStudent,  name="delete_student"),
    path('update_teacher/<str:pk>/', views.UpdateTeacher, name='update_teacher'),


]
