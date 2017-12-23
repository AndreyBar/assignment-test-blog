from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import date
from django.utils import timezone



class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **other_fields):    #birthday, country, city
        """
        Creates and saves a User with the given email, birthday, country, city and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        birthday = None
        city     = None
        country  = None
        if birthday in other_fields:
            birthday = other_fields.get(birthday)
        if city in other_fields:
            city = other_fields.get(city)
        if country in other_fields:
            country = other_fields.get(country)

        user = self.model(
            email=self.normalize_email(email),
            birthday=birthday,
            country=country,
            city=city,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **other_fields):    #birthday, country, city
        """
        Creates and saves a superuser with the given email, birthday, country, city and password.
        """
        birthday = None
        city     = None
        country  = None
        if birthday in other_fields:
            birthday = other_fields.get(birthday)
        if city in other_fields:
            city = other_fields.get(city)
        if country in other_fields:
            country = other_fields.get(country)

        user = self.create_user(
            email,
            password=password,
            birthday=birthday,
            country=country,
            city=city,
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
    email_confirmed = models.BooleanField(default=False)
    birthday        = models.DateField(blank=True, null=True)
    country         = models.CharField(max_length=130, blank=True, null=True)
    city            = models.CharField(max_length=130, blank=True, null=True)
    is_active       = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
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


class Post(models.Model):
    title    = models.CharField(max_length=255)
    date     = models.DateField('Publication date', default=date.today)
    content  = models.TextField(max_length=10000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

class Comment(models.Model):
    user        = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post        = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    text        = models.TextField(max_length=500)
    timestamp   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text[:10]


class Like(models.Model):
    user    = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post    = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
