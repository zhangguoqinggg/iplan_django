"""iplan_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from quote.views import Company_query_list,Logging,Regist
# 导入辅助函数get_schema_view
from rest_framework.schemas import get_schema_view
# 导入两个类
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer

# 利用辅助函数引入所导入的两个类
schema_view = get_schema_view(title='YZDquote',renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('index/', Company_query_list.as_view()),
    re_path('logging/',Logging.as_view()),
    #re_path('^regist/(?P<username>\d+)$',Regist.as_view()),
    re_path('^regist/$',Regist.as_view()),
    path('docs/',schema_view,name='docs') ,
]
