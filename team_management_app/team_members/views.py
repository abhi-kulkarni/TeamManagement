from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import TeamMember
from .forms import TeamMemberForm

class TeamMemberCreateView(CreateView):
    form_class = TeamMemberForm
    success_url = reverse_lazy('list_team_members')

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    success_url = reverse_lazy('list_team_members')

class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('list_team_members')

class TeamMemberListView(ListView):
    model = TeamMember