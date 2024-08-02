from django import forms
from .models import CSVFile

class CSVFileForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ['file']
