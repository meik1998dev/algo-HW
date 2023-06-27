from django.urls import path
from . import views



urlpatterns = [
    path('', views.upload_text_file1, name='upload-text'),
    path('add',views.upload_text_file, name='add'),
    path('addliks',views.upload_text_file1, name='addliks'),
    path('upload-text/', views.upload_text_file, name='upload-text'),
]
