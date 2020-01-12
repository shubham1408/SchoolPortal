"""len URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lenDen.views import ClassroomView, ProblemStatement2, problem_statement3, problem_statement4

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^school/(?P<id>[0-9]+)/$', ClassroomView.as_view(), name='classroom_tabular_view'),
    url(r'^problem/statement/2/$', ProblemStatement2.as_view(), name='problem_statement_2'),
    url(r'^problem/statement/3/$', problem_statement3, name='problem_statement_3'),
    url(r'^problem/statement/4/$', problem_statement4, name='problem_statement_4'),

]
