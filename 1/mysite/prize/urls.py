from django.conf.urls import patterns, url
import views

urlpatterns = [
    url("^$", views.shop, name="prizeindex"),
    url("^register$", views.acc_register, name="register"),
    url("^login", views.acc_login, name="login"),
    url("^logout", views.acc_logout, name="logout"),
    url("^profile", views.profile, name="profile"),
    url("^MyAddressManager", views.MyAddressManager, name="MyAddressManager"),
    url("^ChangePassword", views.ChangePassword, name="ChangePassword"),
    url("^MyOrder", views.MyOrder, name="MyOrder"),
    url("^MyRefunds", views.MyRefunds, name="MyRefunds"),
    url("^MyReservation", views.MyReservation, name="MyReservation"),
    #url("^host_mgr/$", views.host_mgr, name="host_mgr"),

]