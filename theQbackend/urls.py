"""theQbackend URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from testapp.views import savetheevent, showeventdetails, deleteevent, registertheuser, queueenter, queueleave, tokenupdate, queuelength, userqueues

urlpatterns = [
    url(r'api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('neweventdetails/', savetheevent),
    path('showeventdetails/', showeventdetails),
    path('deleteevent/<int:id>/', deleteevent),
    #path('blah/',registertheuser),
    path('queueenter/',queueenter),
    path('queueleave/',queueleave),
    path('tokenupdate/',tokenupdate),
    path('queuedata/',queuelength),
    path('userqueues/',userqueues),
]
