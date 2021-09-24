=============================
Django-response-view-mixin
=============================

.. image:: https://badge.fury.io/py/django-response-mixin-view.svg
    :target: https://badge.fury.io/py/django-response-mixin-view

.. image:: https://travis-ci.org/yourname/django-response-mixin-view.svg?branch=master
    :target: https://travis-ci.org/yourname/django-response-mixin-view

.. image:: https://codecov.io/gh/yourname/django-response-mixin-view/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/yourname/django-response-mixin-view

Your project description goes here

Documentation
-------------

The full documentation is at https://django-response-mixin-view.readthedocs.io.

Quickstart
----------

Install Django-response-view-mixin::

    pip install response-view-mixin

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'response_view_mixin',
        ...
    )

Add Django-response-mixin-view's URL patterns:

.. code-block:: python

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
