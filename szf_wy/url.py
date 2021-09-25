from django.contrib import admin
from django.urls import path, include

import szf_wy.views

urlpatterns = [
    path('transmit', szf_wy.views.transmit_data),

]
