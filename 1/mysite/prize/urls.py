from django.conf.urls import patterns, url
import views

urlpatterns = [
    url("^$", views.shop, name="prize"),
    #url("^host_mgr/$", views.host_mgr, name="host_mgr"),

]