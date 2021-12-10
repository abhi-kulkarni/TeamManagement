from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:    
        model = TeamMember
        fields = '__all__'
        widgets = {
            'is_admin': forms.RadioSelect()
        }
    
    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ''
        