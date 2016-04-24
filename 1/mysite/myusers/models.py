#_*_coding:utf-8_*_
from __future__ import unicode_literals



# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email,name, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have an name')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.create_user(email,
            name = name,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    name = models.CharField(u'名字', max_length=32)
    token = models.CharField(u'token', max_length=128,default=None,blank=True,null=True)
    #department = models.CharField(u'部门', max_length=32,default=None,blank=True,null=True)
    #tel = models.CharField(u'座机', max_length=32,default=None,blank=True,null=True)
    #mobile = models.CharField(u'手机', max_length=32,default=None,blank=True,null=True)
    memo = models.TextField(u'备注', blank=True,null=True,default=None)
    date_joined = models.DateTimeField(blank=True, auto_now_add=True)
    #valid_begin = models.DateTimeField(blank=True, auto_now=True)
    GENDER = (
        ('M', u'男'),
        ('F', u'女'),
    )

    #user = models.OneToOneField(User)
    #user = models.ForeignKey(User, unique=True)
    phonenumber = models.CharField(max_length=11, unique=False,blank=True,null=True,verbose_name='手机号')
    IDcard = models.CharField(max_length=18, unique=False ,blank=True,null=True,verbose_name='身份证')
    gender = models.CharField((u'性别'), max_length=1, choices=GENDER, default='N')
    address = models.CharField(max_length=200,default='',blank=True ,verbose_name='地址')
    QQ = models.CharField(max_length=30, unique=False,verbose_name='QQ号',blank=True,null=True,default='88888888')
    MBWT = models.CharField(max_length=100, unique=False,verbose_name='密保问题',blank=True ,null=True,default='')
    MBDA = models.CharField(max_length=100, unique=False,verbose_name='密保答案',blank=True ,null=True,default='')
    retryCount =  models.IntegerField(verbose_name='出错次数',default=0)



    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

