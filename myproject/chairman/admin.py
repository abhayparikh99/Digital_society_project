from django.contrib import admin
from . models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    exclude = ('created_at','updated_at')
    list_display = ('email','is_active','is_verified','role')
    list_display_links = ('email',)
    list_editable = ('is_active',)
    list_per_page = 5
    search_fields = ('email',)
    list_filter = ('email',)


admin.site.register(User,UserAdmin)
admin.site.register(Chairman)
admin.site.register(Notice)
admin.site.register(MemberDetails)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Complaint)
admin.site.register(Suggestions)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Maintenance)
admin.site.register(Watchman)
admin.site.register(Visitor)
admin.site.register(Transaction)