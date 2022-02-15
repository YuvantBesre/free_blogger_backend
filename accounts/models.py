from django.db import models
from django.contrib.auth.models import AbstractBaseUser,  BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, name, password):
		if not email:
			raise ValueError('User must have an email address')
		if not name:
			raise ValueError('User must have a username')

		user = self.model(
			email=self.normalize_email(email),
			name=name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, name, password):
		user = self.create_user(
			name=name,
			email=self.normalize_email(email),
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=200)
	created = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
	modified = models.DateTimeField(verbose_name='Edited', auto_now_add=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	class Meta:
		ordering = ('-created',)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']

	objects = MyAccountManager()

	def __str__(self):
		return self.email if self.email else '-'

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True


