from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Role(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False, unique=True)

	class Meta:
		ordering = ['id']
		verbose_name = 'Role'
		verbose_name_plural = 'Roles'

	def __str__(self):
		return self.name


# Create your models here.
class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)
    zoom = models.CharField(max_length=255, null=True, blank=True)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE,
								related_name='role', null=True, blank=True)
   
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

