from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500, null=True)
    personal_id = models.SmallIntegerField(null=True)
    father_name = models.CharField(max_length=500, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'last_name', 'personal_id', 'father_name', 'date_of_birth']

    def __str__(self):
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


class ValidateCode(models.Model):
    token = models.CharField(max_length=200)
    email = models.EmailField()
    code = models.SmallIntegerField()
    expration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
