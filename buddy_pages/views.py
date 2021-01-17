from django.shortcuts import render

# Create your views here.

def home_screen_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Home"

	user = request.user

	if user.is_authenticated:
		print(user.first_name)
		context['user'] = user

	return render(request, "buddy_pages/home.html", context)