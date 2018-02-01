from django.db import models

# Create your models here.

from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)

def user_directory_path(instance, filename):
	ext = filename.split(".")[-1]
	return "user_{0}/{1}".format(instance.user.id, ext)

class UserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password=None, is_active=True, is_staff=False, is_admin=False):
		"""
		Creates and saves a new User with the given email, first name, last name and password
		"""
		if not email:
			raise ValueError('Users must have an email address')
		if not password:
			raise ValueError('Users must provide a password')

		user = self.model(
				email=self.normalize_email(email)
			)
		user.set_password(password)
		user.first_name = first_name
		user.last_name = last_name
		user.active = is_active
		user.staff = is_staff
		user.admin = is_admin
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, password):
		"""
		Creates and saves a staff user with the given email and password.
		"""
		user = self.create_user(
			email,
			first_name=first_name,
			last_name=last_name,
			password=password,
		)
		user.staff = True
		user.save(using=self._db)
		return user

	def create_superuser(self, email, first_name, last_name, password=None):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
			email,
			first_name=first_name,
			last_name=last_name,
			password=password,
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name = 'email address',
		max_length=255,
		unique=True,
		error_messages={'unique': 'A user with the email address already exists.'}
		)
	first_name = models.CharField(
		verbose_name='first name',
		max_length=255,
		blank = False,
		error_messages={
            'blank': 'First name must be provided.'}
		)
	last_name = models.CharField(
		verbose_name='last name',
		max_length=255,
		blank = False,
		error_messages={
            'blank': 'Last name must be provided.'}
		)

	profile_pic = models.ImageField(upload_to=user_directory_path, blank=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # A admin, non-super user
	admin = models.BooleanField(default=False) # A super user

	timestamp = models.DateTimeField(auto_now_add=True) # Time user was created
	updated_time = models.DateTimeField(auto_now=True) # Time user was updated

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name'] 

	objects = UserManager()

	def get_short_name(self):
		return self.first_name

	def get_full_name(self):
		return "%s %s" % self.first_name, self.last_name

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
		return self.staff

	@property
	def is_active(self):
		return self.active

	@property
	def is_admin(self):
		return self.admin
