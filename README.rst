===============
Dummy Connector
===============

This project is a dummy module for Django Trigger Happy that can be used 
to bootstrap a new Service. 

All you need to do will be to replace "dummy" everywhere and provide
all the needed stuff in my_dummy.py module to handle the data to/from 
the service you want to plug to DTH. Even this README.rst should be adapted.


Requirements :
==============
* django_th: 0.9.0


Installation:
=============
to get the project, from your virtualenv, do :

.. code:: python

    pip install django-th-dummy
    
then do

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

TH_SERVICES is a list of the services used by Trigger Happy

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
