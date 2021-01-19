from django.db import models
from django.conf import settings
from account.models import CustomUser

# Create your models here.

#Daily Sessions
class Daily_Session(models.Model):
	date = models.DateField(verbose_name="Date", null=False, blank=False)
	time = models.CharField(max_length=100, null=False, blank=False)
	completed = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
	last_updated = models.DateTimeField(auto_now=True, verbose_name="last updated")

	def __str__(self):
		return self.date.strftime("%A - %B, %d") + " @ " + self.time

	class Meta:
		verbose_name = 'Daily Session'
		verbose_name_plural = 'Daily Sessions'

#Session Sign ins
class Session_SignIn(models.Model):
	sessionID = models.ForeignKey(Daily_Session, on_delete=models.CASCADE,
									related_name='session', null=False, blank=False)

	userID = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
									related_name='user', null=False, blank=False)
	date_created = models.DateTimeField(auto_now_add=True, verbose_name="date created")
	last_updated = models.DateTimeField(auto_now=True, verbose_name="last updated")

	class Meta:
		verbose_name = 'Session Sign In'
		verbose_name_plural = 'Session Sign Ins'





