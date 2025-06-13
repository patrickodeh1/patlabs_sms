from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, user_type, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not user_type:
            raise ValueError('Users must have a user type')
        
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, full_name, user_type='ADMIN', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, full_name, user_type, password, **extra_fields)
    