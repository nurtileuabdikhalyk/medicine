from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('consultation/', home, name="consultation"),
    path('zapis/', home, name="zapis"),
    path('call/', home, name="call"),
    path('call_district_doctor/', call_district_doctor, name="call_district_doctor"),
    path('record_district_doctor/', record_district_doctor, name="record_district_doctor"),
    path('data/', data, name="data"),
    path('record/', record, name="record"),
    path('card/', card, name="card"),
    path('feedback/', feedback, name="feedback"),
    path('accounts/signup/', account_signup, name='account_signup'),
    path('accounts/login/', account_login, name='account_login'),
]
