from django.contrib import admin

from accounts.models import Connector, Participation, Profile, Transport

admin.site.register(Profile)  # FIXME extend user admin
admin.site.register(Participation)
admin.site.register(Transport)
admin.site.register(Connector)
