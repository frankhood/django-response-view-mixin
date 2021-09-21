# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django_response_mixin_view.urls', namespace='django_response_mixin_view')),
    url(r'^tests/', include('tests.example.urls'))
]
