from django.urls import path

from buddy_sessions.views import (
    main_room_view,
    welcome_screen_view,
    testing_view,
    zoom_testing_view,
    data_zoom_testing_view,
)

app_name = 'buddy_sessions'

urlpatterns = [
    path('main_room/', main_room_view, name="main_room"),
    path('welcome/', welcome_screen_view, name="welcome"),
    path('test/', testing_view, name="testing"),
    path('zoom/', data_zoom_testing_view, name="zoom"),
    path('zoom2/', zoom_testing_view, name="zoom2"),
 ]