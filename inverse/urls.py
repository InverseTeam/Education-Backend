"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include, re_path
from inverse.settings import MEDIA_ROOT, MEDIA_URL
from users.views import *
from sections.views import *
from news.views import *
from textbooks.views import *
from rest_framework import routers
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title='Inverse.Образование API',
      default_version='v1',
      description='Платформа для записи в дополнительные образовательные секции.',
      terms_of_service='https://www.google.com/policies/terms/',
      contact=openapi.Contact(email='belogurov.ivan@list.ru'),
      license=openapi.License(name='BSD License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Users
    path('api/users/roles/', RoleAPIListView.as_view()),
    path('api/users/auth/', include('djoser.urls')),
    re_path(r'^api/users/auth/', include('djoser.urls.authtoken')),

    # Sections
    path('api/sections/create/', SectionAPICreateView.as_view()),
    path('api/sections/', SectionAPIListView.as_view()),
    path('api/sections/load/', SectionAPILoadListView.as_view()),
    path('api/sections/<int:pk>/', SectionAPIDetailView.as_view()),
    path('api/sections/groups/create/', GroupAPICreateView.as_view()),
    path('api/sections/groups/schedules/create/', ScheduleAPICreateView.as_view()),
    path('api/sections/<int:pk>/applications/create/', ApplicationAPICreate.as_view()),
    path('api/sections/applications/my/', ApplicationAPIMyListView.as_view()),
    path('api/sections/applications/<int:pk>/confirm/', ApplicationAPIConfirmView.as_view()),
    path('api/sections/applications/<int:pk>/refuse/', ApplicationAPIRefuseView.as_view()),
    path('api/sections/<int:pk>/homeworks/create/', HomeworkAPICreateView.as_view()),
    path('api/sections/homeworks/my/', HomeworkAPIMyListView.as_view()),
    path('api/sections/<int:pk>/grades/create/', GradeAPICreateView.as_view()),
    path('api/sections/grades/my/', GradeAPIMyListView.as_view()),
    path('api/sections/categories/', CategoryAPIListView.as_view()),

    # Textbooks
    path('api/textbooks/create/', TextbookAPICreateView.as_view()),
    path('api/textbooks/', TextbookAPIListView.as_view()),

    # News
    path('api/news/create/', NewAPICreateView.as_view()),
    path('api/news/', NewAPIListView.as_view()),
    path('api/news/tags/', TagAPIListView.as_view()),

    # Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
