from django.urls import path
from .views import TeamMemberCreateView, TeamMemberDeleteView, TeamMemberListView, TeamMemberUpdateView

urlpatterns = [
    path('', TeamMemberListView.as_view(template_name='team_members/team_members.html'), name='list_team_members'),
    path('team_members/add/', TeamMemberCreateView.as_view(template_name='team_members/add_team_member.html'), name='add_team_member'),
    path('team_members/edit/<int:pk>/', TeamMemberUpdateView.as_view(template_name='team_members/edit_team_member.html'), name='edit_team_member'),
    path('team_members/delete/<int:pk>/', TeamMemberDeleteView.as_view(), name='delete_team_member'),
]