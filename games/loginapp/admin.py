from django.contrib import admin
from loginapp.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):

    pass

admin.site.register(User, UserAdmin)




