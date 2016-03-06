# django imports

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

#  imports
from myusers.models import MyUserManager,MyUser





def create_myuser(email,name,date_of_birth,password=None):
    """Creates a customer for the given request (which means for the current
    logged in user/or the session user).

    This shouldn't be called directly. Instead get_or_create_customer should be
    called.
    """
    myuser = MyUserManager.create_user(email,name,date_of_birth,password)
    return myuser






