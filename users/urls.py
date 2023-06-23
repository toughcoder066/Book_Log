from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from users import views


urlpatterns=[
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='/'),name='logout'),
    path('register', views.register, name='register'),
]