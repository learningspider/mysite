# django imports

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

#  imports
from myusers.models import MyUserManager,MyUser

def get_or_create_myuser(request):
    """Get or creates the customer object.
    """
    myuser = get_myuser(request)
    if myuser is None:
        myuser = request.myuser = create_myuser(request)

    return myuser



def create_myuser(userName,password,name="",date_of_birth=""):
    """Creates a customer for the given request (which means for the current
    logged in user/or the session user).

    This shouldn't be called directly. Instead get_or_create_customer should be
    called.
    """
    myuser = MyUserManager.create_user(userName,name,date_of_birth,password)
    return myuser


def get_myuser(request):
    try:
        return request.myuser
    except AttributeError:
        myuser = request.myuser = _get_myuser(request)
        return myuser

def _get_myuser(request):
    user = request.user
    if user.is_authenticated():
        try:
            return MyUser.objects.get(email=request.MyUser.email)
        except ObjectDoesNotExist:
            return None


'''def update_myuser_after_login(request):
    """Updates the customer after login.

    1. If there is no session customer, nothing has to be done.
    2. If there is a session customer and no user customer we assign the session
       customer to the current user.
    3. If there is a session customer and a user customer we copy the session
       customer information to the user customer and delete the session customer
    """
    try:
        session_customer = Customer.objects.get(session=request.session.session_key)
        try:
            user_customer = Customer.objects.get(user=request.user)
        except ObjectDoesNotExist:
            session_customer.user = request.user
            session_customer.save()
        else:
            user_customer.selected_shipping_method = session_customer.selected_shipping_method
            user_customer.save()
            session_customer.delete()
    except ObjectDoesNotExist:
        pass


def create_unique_username(email):
    new_email = email[:30]
    cnt = 0
    while User.objects.filter(username=new_email).exists():
        cnt += 1
        new_email = '%s%.2d' % (new_email[:28], cnt)
    return new_email'''

