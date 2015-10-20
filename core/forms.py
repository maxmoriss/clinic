from django import forms
from django.conf import settings

from core.models import Entry


class EntryForm(forms.ModelForm):
    class Meta(object):
        model = Entry
        fields = ('doctor', 'patient', 'start_at',)
        widgets = {
            'patient': forms.TextInput(
                attrs={'placeholder': 'Фамилия Имя Отчество'}
            ), 
        }
