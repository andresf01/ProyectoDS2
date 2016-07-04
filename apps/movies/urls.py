from django.conf.urls import url
import views

urlpatterns = [
    url(r'^movie/(?P<movie_id>.*$)', views.movie),
    url(r'^search$', views.search),
    url(r'^mylists/$', views.mylist),
    url(r'^mylists/(?P<list_id>.*$)', views.user_list),
    url(r'^test$', views.testApi),
    
]