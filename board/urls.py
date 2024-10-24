from django.urls import path, include
from board import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:text_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:text_id>/update', views.update, name='update'),
    path('<int:text_id>/delete', views.delete, name='delete'),
    path('<int:text_id>/comment_create', views.comment_create, name='comment_create'),
]