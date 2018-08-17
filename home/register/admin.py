from django.contrib import admin
from .models import register_user, register_pg

admin.site.register(register_user)
admin.site.register(register_pg)




