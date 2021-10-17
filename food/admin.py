from django.contrib import admin
from food.models import UserProfile

#admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','location','post','phone')

    def user_info(self ,obj):
        return obj.description

admin.site.register(UserProfile, UserProfileAdmin)