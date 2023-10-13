from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id','status','visits','team_presence')

admin.site.register(Project,ProjectAdmin)
# Register your models here.
