from django.urls import path, include
from member import views

app_name ="member"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout', views.logout, name='logout'),
]