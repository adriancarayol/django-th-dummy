# -*- coding: utf-8 -*-

# django classes
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.log import getLogger

# add the python API here if needed
from external_api import CallOfApi

# django_th classes
from django_th.services.services import ServicesMgr
from django_th.models import UserService, ServicesActivated

"""
    handle process with dummy
    put the following in settings.py

    TH_DUMMY = {
        'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
    }

"""

logger = getLogger('django_th.trigger_happy')


class ServiceDummy(ServicesMgr):

    def process_data(self, token, trigger_id, date_triggered):
        """
            get the data from the service
        """
        datas = list()
        return datas

    def save_data(self, token, trigger_id, **data):
        """
            let's save the data
        """
        from th_dummy.models import Dummy

        if token and 'link' in data and data['link'] is not None and len(data['link']) > 0:
            # get the data of this trigger
            trigger = Dummy.objects.get(trigger_id=trigger_id)

            # get the token of the external service for example
            dummy_instance = external_api.CallOfApi(
                settings.TH_DUMMY['consumer_key'], token)

            title = ''
            title = (data['title'] if 'title' in data else '')
            # add data to the external service
            item_id = dummy_instance .add(
                url=data['link'], title=title, tags=(trigger.tag.lower()))

            sentance = str('dummy {} created').format(data['link'])
            logger.debug(sentance)
        else:
            logger.critical("no token provided for trigger ID %s ", trigger_id)

    def auth(self, request):
        """
            let's auth the user to the Service
        """
        callbackUrl = 'http://%s%s' % (
            request.get_host(), reverse('dummy_callback'))

        request_token = CallOfApi.get_request_token(
            consumer_key=settings.TH_DUMMY['consumer_key'],
            redirect_uri=callbackUrl)

        # Save the request token information for later
        request.session['request_token'] = request_token

        # URL to redirect user to, to authorize your app
        auth_url = CallOfApi.get_auth_url(
            code=request_token, redirect_uri=callbackUrl)

        return auth_url

    def callback(self, request):
        """
            Called from the Service when the user accept to activate it
        """

        try:
            # finally we save the user auth token
            # As we already stored the object ServicesActivated
            # from the UserServiceCreateView now we update the same
            # object to the database so :
            # 1) we get the previous objet
            us = UserService.objects.get(
                user=request.user,
                name=ServicesActivated.objects.get(name='ServiceDummy'))
            # 2) then get the token
            access_token = CallOfApi.get_access_token(
                consumer_key=settings.TH_DUMMY['consumer_key'],
                code=request.session['request_token'])

            us.token = access_token
            # 3) and save everything
            us.save()
        except KeyError:
            return '/'

        return 'dummy/callback.html'
