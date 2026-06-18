"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path

from home.views import home_page_view
from catalog.views import catalog_page_view
from question.views import question_page_view,generate,check
from guide.views import guide_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),
    path('/catalog/', catalog_page_view, name='catalog'),
    path('guide/<str:group_type>/',guide_page_view,name='guide'),
    path('/question/<str:group_type>/', question_page_view, name='question'),

    path('api/generate/<str:group_type>/<int:difficulty>/',generate, name='question_generate'),
    path('api/check/<str:question>/<str:answer>/', check , name='answer_check')
]
