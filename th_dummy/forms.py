# -*- coding: utf-8 -*-

from django import forms
from th_Dummy.models import Dummy


class DummyForm(forms.ModelForm):

    """
        for to handle Pocket service
    """

    class Meta:
        model = Dummy
        fields = ('tag',)


class DummyProviderForm(DummyForm):
    pass


class DummyConsummerForm(DummyForm):
    pass
