from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    user_in_migrations = True

    def _create_user(self, identity_number, password, **extra_fields):

        if not identity_number:
            raise ValueError('The given identity number must be set')
        user = self.model(identity_number=identity_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, identity_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(identity_number, password, **extra_fields)

    def create_superuser(self, identity_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(identity_number, password, **extra_fields)
