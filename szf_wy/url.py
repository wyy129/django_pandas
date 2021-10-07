from django.urls import path

import szf_wy.views

urlpatterns = [
    path('index', szf_wy.views.index),
    path('transmit', szf_wy.views.transmit_data),
    path('login', szf_wy.views.login_in),
    path('register', szf_wy.views.register),
    # path('login', szf_wy.views.LoginClassViews.as_view(), name='login'),

]
