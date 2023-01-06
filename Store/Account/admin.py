from django.contrib import admin


"""import models"""


from.models import UserProfile


"""show model"""


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('author', 'phone_number', 'home_address')


admin.site.register(UserProfile, UserProfileAdmin)



