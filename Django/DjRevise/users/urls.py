from django.urls import path
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',views.register,name='user_register'),
    path('profile/',views.profile,name='user_profile'),
    # path('login/',views.login,name='user_login'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='user_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='user_logout'),   
]

