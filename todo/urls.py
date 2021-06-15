from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<uuid:id>/', views.deleteTask, name="delete"),
    path('delete-all/', views.deleteAll, name="deleteAll"),
    path('rename-task/<uuid:id>/', views.renameTask, name="renameTask"),


    path('status-just-added/<uuid:id>/', views.statusJustAdded, name="statusJustAdded"),
    path('status-pending/<uuid:id>/', views.statusPending, name="statusPending"),
    path('status-completed/<uuid:id>/', views.statusCompleted, name="statusCompleted"),
]
