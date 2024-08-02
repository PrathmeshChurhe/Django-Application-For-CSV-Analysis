from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('process/<int:pk>/', views.process_file, name='process_file'),]
