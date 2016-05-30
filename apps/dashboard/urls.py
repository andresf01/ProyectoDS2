from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^index_new$', views.index_new)
]