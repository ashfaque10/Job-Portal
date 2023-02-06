"""jobproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from jobapp import views

urlpatterns = [
    path('',views.index),
    path('register/',views.register),
    path('login/',views.login),
    path('postj/<str:username>',views.postj),
    path('clog/',views.clog),
    path('company/',views.company),
    path('creg/',views.creg),
    path('tokens/',views.verify),
    path('success/',views.success),
    path('verifyy/<auth_token>',views.verifyy),
    path('error/',views.error),
    path('editprofile/<str:mail>/<str:token>',views.editprofile),
    path('rcompany/',views.rcompany),
    path('disp/',views.disp),
    path('viewp/<int:id>',views.viewp),
    path('userp/',views.userp),
    path('userapply/<int:id>',views.userapply),
    path('viewa/<str:username>',views.view_applicants)
]
