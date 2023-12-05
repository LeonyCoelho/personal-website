from django import forms
from .models import Project, ProjectImage

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, value, initial):
        return super().clean(value, initial)

class ProjectForm(forms.ModelForm):
    images = MultipleFileField(required=False)

    class Meta:
        model = Project
        fields = ['project_title', 'project_tags', 'project_description', 'project_images']

    def clean_images(self):
        images = self.cleaned_data.get('images')
        if images:
            return [ProjectImage(project_image=image) for image in images]
        return []
