from django.shortcuts import render, redirect
from .models import Session_SignIn
from .models import Daily_Session
from .forms import Session_SignIn_Form

from account.models import CustomUser
from account.models import Role
from django.contrib.sessions.models import Session
from django.utils import timezone

from buddy_sessions import signature


#Welcome View to join session
def welcome_screen_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Welcome"

	user = request.user

	if user.is_authenticated:
		context['user'] = user
		sessions = Daily_Session.objects.filter(completed=False).order_by('date', 'time')
		
		next_session = sessions.first()

		if request.POST:
			form = Session_SignIn_Form(request.POST)
			if form.is_valid:
				signins_current_session = Session_SignIn.objects.filter(sessionID=next_session.id, userID=user.id)

				for signin in signins_current_session:
					print(signin)

				if signins_current_session.count() == 1:
					return redirect('/sessions/main_room/')
				else:
					form.save()
					return redirect('/sessions/main_room/')
			else:
				print("not valid")
				print(form.errors)				
		else:
			form = Session_SignIn_Form(
				initial= {
					"sessionID": next_session.id,
					"userID": user.id
				})

		context['form'] = form

	return render(request, "buddy_sessions/welcome.html", context)


#Main room
def main_room_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Main Room"

	user = request.user
	context['user'] = user


	return render(request, "buddy_sessions/main_room.html", context)



#ZOOM TESTING
def data_zoom_testing_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Zoom Test 1"

	user = request.user
	context['user'] = user

	data = {'apiKey': "j7XxMYSmS9mlFr05ycOXhw" ,
    'apiSecret': "LlDRXl0DFJjxygPxzfxjKLRzlFxVmUuyyczm",
    'meetingNumber': 9859719154,
    'role': 0}
	print (signature.generateSignature(data))

	context['signature'] = signature.generateSignature(data)

	return render(request, "buddy_sessions/room_data.html", context)


def zoom_testing_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Zoom Test 2"

	user = request.user
	context['user'] = user

	return render(request, "buddy_sessions/zoom_test.html", context)


#Testing Logged in users

def get_current_users():
	all_sessions = Session.objects.all()
	for session in all_sessions:
		data = session.get_decoded()
		# print(data.get('_auth_user_id', None))

	active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
	user_id_list = []

	for session in active_sessions:
		data = session.get_decoded()
		user_id_list.append(data.get('_auth_user_id', None))

	# Query all logged in users based on id list
	return CustomUser.objects.filter(id__in=user_id_list)

def all_students_logged_in():
	users = get_current_users()
	student_role = Role.objects.get(name="Student")	
	students= users.filter(roleId=student_role.id)
	return students

def all_volunteers_logged_in():
	users = get_current_users()
	volunteer_role = Role.objects.get(name="Volunteer")
	volunteers= users.filter(roleId=volunteer_role.id)
	return volunteers

def all_staff_logged_in():
	users = get_current_users()
	staff_role = Role.objects.get(name="Staff")
	staff = users.filter(roleId=staff_role.id)
	return staff

#Testing
def logout_student():
	print("logout students")

def logout_staff():
	print("logout staff")

def logout_volunteers():
	print("logout volunteers")

#Testing Sessions
def testing_view(request, *args, **kwargs):	
	context = {}
	context['page_title'] = "Main Room"
	user = request.user
	context['user'] = user
	context['staff'] = all_staff_logged_in()
	context['students'] = all_students_logged_in()
	context['volunteers'] = all_volunteers_logged_in()

	return render(request, "buddy_sessions/testing.html", context)




