"""
URL configuration for DjRevise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

# this below two line are include in order to show the images on the website.
from django.conf import settings
from django.conf.urls.static import static
# from post import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('post.urls')),
    path('user/',include('users.urls')),
    # path('',post_views.home,name='post_home'),
    # path('about/',post_views.about,name='post_about'),
]

# if the DEBUG == True, this way the images are show on the gui if debug is on.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    