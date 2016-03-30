from django.conf.urls import patterns, url
import views

urlpatterns = [
    url("^$", views.shop, name="prize"),
    url("^register$", views.register, name="prize"),
    url("^login", views.login, name="prize"),
    #url("^host_mgr/$", views.host_mgr, name="host_mgr"),

]