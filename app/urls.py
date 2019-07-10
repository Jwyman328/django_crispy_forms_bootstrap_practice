"""practice_full_boot_crisp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage_view.as_view(), name='home'),
    path('mailing_list', views.Mail_list_page_view.as_view(), name='mailing_list'),
    path('all_blogs', views.All_blogs_page_view.as_view(), name='all_blogs'),
    path('create_blog', views.Createpage_view.as_view(), name='create_blog'),
    path('about', views.Aboutpage_view.as_view(), name='about'),
    path('post/<int:pk>/', views.Postpage_view.as_view(), name='post'),

  
]
