from django.shortcuts import render, redirect

# Home screen view
def home_screen_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Home"

	user = request.user

	if user.is_authenticated:
		context['user'] = user

	return render(request, "buddy_pages/home.html", context)