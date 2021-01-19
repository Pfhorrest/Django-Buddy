from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.sessions.models import Session
from .models import UserSession
from .models import CustomUser
 
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
	UserSession.objects.get_or_create(user = user, session_id = request.session.session_key)


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
	print('user logged out')
	user_sessions = UserSession.objects.filter(user = user)
	for user_session in user_sessions:
		user_session.session.delete()
	



##Session storage checks
	# all_sessions = Session.objects.all()
	# for session in all_sessions:
	# 	print()
	# 	print(session)
	# 	data = session.get_decoded()
	# 	print(data.get('id'))
	# 	print(data.get('_auth_user_id', None))
	# 	print()


	# user_sessions = UserSession.objects.all()
	# for session in user_sessions:
	# 	print()
	# 	print(session.user.id)
	# 	print(session.user)
	# 	print(session.session)
	# 	print()