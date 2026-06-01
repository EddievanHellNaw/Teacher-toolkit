from students import views
from django.urls import path

urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('create/', views.student_create, name='student_create'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
    path('<int:student_id>/edit/', views.student_edit, name='student_edit'),
    path('<int:student_id>/delete/', views.student_delete, name='student_delete'),
    
]