from django.contrib import admin

from .models import TeamMember


class TeamMemberAdmin(admin.ModelAdmin):
    fields = ['__all__']

admin.site.register(TeamMember, TeamMemberAdmin)