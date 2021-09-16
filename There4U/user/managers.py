from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    """
    Manager class for custom user model.
    """
    def create_user(self, email, password, **extra_fields):
        '''Create a user.'''
        if not email:
            raise ValueError('User should enter an email address')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''Create a superuser.'''
        return self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields,
            is_admin=True,
            is_staff=True,
            is_superuser=True
        )
