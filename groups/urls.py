from groups import views
from django.urls import path

urlpatterns = [
    path('', views.groups_list, name='groups_list'),
    path('create/', views.group_create, name='group_create'),
    path('<int:group_id>/edit/', views.group_edit, name='group_edit'),
    path('<int:group_id>/', views.group_detail, name='group_detail'),
    path('<int:group_id>/delete/', views.group_delete, name='group_delete'),
]