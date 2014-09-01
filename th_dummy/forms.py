# -*- coding: utf-8 -*-

from django import forms
from django.forms import TextInput
from th_dummy.models import Dummy


class DummyForm(forms.ModelForm):

    """
        for to handle Pocket service
    """

    class Meta:
        model = Dummy
        fields = ('name',)
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class DummyProviderForm(DummyForm):
    pass


class DummyConsumerForm(DummyForm):
    pass
