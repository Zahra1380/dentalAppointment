from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth=None, name=None, last_name=None, personal_id=None, father_name=None, password=None):
        """
        Creates and saves a User with the
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            last_name=last_name,
            personal_id=personal_id,
            father_name=father_name,
            date_of_birth=date_of_birth
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, father_name,date_of_birth, name, last_name, email, personal_id, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            last_name=last_name,
            personal_id=personal_id,
            father_name=father_name,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user