# -*- coding: utf-8 -*-

from django.db import models
from django_th.models.services import Services


class Dummy(Services):

    # put whatever you need  here
    # eg title = models.CharField(max_length=80)
    # but keep at least this one
    trigger = models.ForeignKey('TriggerService')

    class Meta:
        app_label = 'django_th'

    def __unicode__(self):
        return "%s" % (self.name)

    def show(self):
        return "My Dummy %s" % (self.name)
