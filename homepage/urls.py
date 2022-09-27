from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),        #http://127.0.0.1:8000/homepage/
    path('qwe/', qwe, name='qwe'),      #http://127.0.0.1:8000/homepage/qwe/
    path('docker/', docker, name='docker'),
    path('systemd/', systemd, name='systemd'),
]