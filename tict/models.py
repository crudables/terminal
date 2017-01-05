from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from .utils import UserManager

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
        USERNAME_FIELD = 'email'
        SEX_CHOICE = (('male','Male'),('female','Female'),)
        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=30,default='your own name')
        last_name = models.CharField(max_length = 30,default='your surname')
        other_names = models.CharField(max_length = 255,default='other name')
        username = models.CharField(max_length=30,unique=True)
        staff_id = models.CharField(max_length=7,unique=True,blank=True)
        bio = models.TextField()
        department = models.CharField(max_length=30)
        date_of_entry = models.DateField(default=timezone.now)
        date_registered = models.DateField(default=timezone.now)
        phone_number= models.CharField(max_length=12)
        sex = models.CharField(max_length=6,choices=SEX_CHOICE,default='male')
        is_active = models.BooleanField(default=True)
        staff = models.BooleanField(default=False)

        class Meta:
            ordering = ('staff_id',)
        def get_full_name(self):
            return self.first_name+' '+self.last_name

        def get_short_name(self):
            return self.first_name

        def __str__(self):
            return self.get_full_name

        objects  = UserManager()
