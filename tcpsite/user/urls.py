from django.conf.urls import url
from . import views


app_name = 'user'

urlpatterns = [
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
]
