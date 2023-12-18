from django.db import models

# Create your models here.
class Institute_regis(models.Model):
    def create_user(self, username, password=None, user_type=None, **extra_fields):
        user = self.model(username=username, user_type=user_type, **extra_fields)
        user.set_password(password)
        print(f"Password before save: {user.password}")
        user.save(using=self._db)
        print(f"Password after save: {user.password}")
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 4)
        return self.create_user(username, password, **extra_fields)
    
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,Group

class CustomUserManager(BaseUserManager):
    