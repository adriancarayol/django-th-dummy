=====================================
Django Trigger Happy : Dummy Service
=====================================

This service provides an acces to your Dummy account from Trigger Happy

Requirements :
==============
* django_th: 0.8.1


Installation:
=============
to get the project, from your virtualenv, do :

.. code:: python

    pip install django-th-dummy
    
then

.. code:: python

    python manage.py syncdb

to startup the database

Parameters :
============
As usual you will setup the database parameters.

Important parts are the settings of the available services :

Settings.py 
-----------

INSTALLED_APPS
~~~~~~~~~~~~~~

add the module th_rss to INSTALLED_APPS

.. code:: python

    INSTALLED_APPS = (
        'th_dummy',
    )    

TH_SERVICES 
~~~~~~~~~~~

TH_SERVICES is a list of the services use by Trigger Happy

.. code:: python

    TH_SERVICES = (
        'th_dummy.my_dummy.ServiceDummy',
    )

TH_DUMMY
~~~~~~~~~~~
TH_DUMMY is the settings you will need to be able to add/read data in/from Dummy Service.

.. code:: python

    TH_DUMMY = {
        'consumer_key': 'abcdefghijklmnopqrstuvwxyz',
    }

Setting up : Administration
===========================

once the module is installed, go to the admin panel and activate the service dummy. 

All you can decide here is to tell if the service requires an external authentication or not.

Once they are activated. User can use them.
