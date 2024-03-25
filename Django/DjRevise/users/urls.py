from django.urls import path
from users import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',views.register,name='user_register'),
    path('profile/',views.profile,name='user_profile'),
    # path('login/',views.login,name='user_login'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='user_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='user_logout'),   
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),name='password_reset'),   
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),name='password_reset_done'),   
# {% url 'password_reset_confirm' uidb64=uid token=token %}
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),name='password_reset_confirm'),   
    
]

