"""myproject URL Configuration

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
from views import callback,callback1,fetchhaha,callback2,upload_json,uploadtotable,fetchhah,deletae,callback3,deletat
urlpatterns = [
    url(r'^admin/', admin.site.urls),
     url(r'^callback$', view=callback, name='callback'),
       url(r'^callback1$', view=callback1, name='callback1'),
        url(r'^callback2$', view=callback2, name='callback2'),
              url(r'^callback3$', view=callback3, name='callback3'),
        url(r'^fetch$', view=fetchhaha, name='fetch'),
          url(r'^upload$', view=upload_json, name='up'),
           url(r'^uplod$', view=uploadtotable, name='upload'),
              url(r'^fetchmed$', view=fetchhah, name='fetch1'),
              url(r'^delete$', view=deletae, name='fetch2123'),
                 url(r'^deletet$', view=deletat, name='deletet'),

]
