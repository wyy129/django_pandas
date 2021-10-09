from django.urls import path

import szf_wy.views

urlpatterns = [
    path('', szf_wy.views.index),
    path('transmit_data', szf_wy.views.transmit_data),
    path('login', szf_wy.views.Login.as_view(),name='login_in'),
    path('register', szf_wy.views.register),
    path('get_username', szf_wy.views.get_username),

]
