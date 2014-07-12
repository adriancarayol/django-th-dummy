# -*- coding: utf-8 -*-

from django import forms
from django.forms import TextInput
from th_Dummy.models import Dummy


class DummyForm(forms.ModelForm):

    """
        for to handle Pocket service
    """

    class Meta:
        model = Dummy
        fields = ('tag',)
        widgets = {
            'tag': TextInput(attrs={'class': 'form-control'}),
        }


class DummyProviderForm(DummyForm):
    pass


class DummyConsumerForm(DummyForm):
    pass
