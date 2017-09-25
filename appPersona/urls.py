#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      andres
#
# Created:     21/08/2017
# Copyright:   (c) andres 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from django.conf.urls import url
from appPersona.views import index

urlpatterns = [
    url('index/',index)
]