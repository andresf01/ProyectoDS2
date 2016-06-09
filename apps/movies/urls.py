from django.conf.urls import url
import views

urlpatterns = [
    url(r'^movie/(?P<movie_id>.*$)', views.movie),
    url(r'^search$', views.search),
    url(r'^mylist$', views.mylist),
    url(r'^test$', views.testApi)
]