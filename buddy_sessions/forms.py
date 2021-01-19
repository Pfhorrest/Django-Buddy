from django import forms
from buddy_sessions.models import Session_SignIn

class Session_SignIn_Form(forms.ModelForm):
	class Meta:
		model = Session_SignIn
		fields = ('sessionID', 'userID')