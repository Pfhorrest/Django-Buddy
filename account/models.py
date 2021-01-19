from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.sessions.models import Session

#User Role in organization
class Role(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False, unique=True)

	class Meta:
		ordering = ['id']
		verbose_name = 'Role'
		verbose_name_plural = 'Roles'

	def __str__(self):
		return self.name

#Custom User
class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)
    zoom = models.CharField(max_length=255, null=True, blank=True)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE,
								related_name='role', null=True, blank=True)
   
    def __str__(self):
        return self.username

#token for authorization
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)



# Model to store the list of logged in users
class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)



# User Log of times in and out
class User_Log(models.Model):
	userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
									related_name='user_log', null=False, blank=False)
	time_in = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	time_out = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
	last_updated = models.DateTimeField(auto_now=True, verbose_name="last updated")

	class Meta:
		verbose_name = 'User Log'
		verbose_name_plural = 'User Logs'




