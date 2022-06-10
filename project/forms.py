from django import forms
from django.forms import ModelForm, widgets
from . models import Project

class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'project_img','source_code_url', 'demo_code_url', 'tags'
        ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'})
            

        # self.fields['name'].widget.attrs.update({
        #         'class': 'input'
        #     })            
