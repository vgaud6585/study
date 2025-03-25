from django import forms
from .models import StudyRecords

class StudyForm(forms.ModelForm):
  class Meta:
    model = StudyRecords
    fields = ['usr_head', 'usr_heading', 'usr_description', 'usr_code_box',]