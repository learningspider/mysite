from django.conf.urls import patterns, url
import views

urlpatterns = [
    url("^$", views.shop, name="prizeindex"),
    url("^register$", views.acc_register, name="register"),
    url("^login", views.acc_login, name="login"),
    url("^loginout", views.acc_logout, name="loginout"),
    #url("^host_mgr/$", views.host_mgr, name="host_mgr"),

]