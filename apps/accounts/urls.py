from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.user_login),
    url(r'^logout$', views.user_logout),
    url(r'^signup$', views.signup),
    url(r'^account$', views.account),
    url(r'^statistics$', views.statistics),
]