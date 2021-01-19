from django.contrib import admin
from buddy_sessions.models import Daily_Session
from buddy_sessions.models import Session_SignIn

# Register your models here.


class Daily_Session_Admin(admin.ModelAdmin):
    list_display = ('date', 'time')
    search_fields = ()
    readonly_fields=()
    filter_horizontal = ()

admin.site.register(Daily_Session, Daily_Session_Admin)


class Session_SignIn_Admin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
    readonly_fields=()
    filter_horizontal = ()

admin.site.register(Session_SignIn, Session_SignIn_Admin)