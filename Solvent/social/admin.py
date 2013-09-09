from django.contrib import admin
from Solvent.social.models import User, Project, Attachment

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_active')

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_activity')

class AttachmentAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_modified', 'dataOverview')


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Attachment, AttachmentAdmin)

