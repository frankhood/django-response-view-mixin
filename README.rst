=============================
Django-response-view-mixin
=============================

.. image:: https://badge.fury.io/py/django-response-mixin-view.svg
    :target: https://badge.fury.io/py/django-response-mixin-view

.. image:: https://github.com/frankhood/django-response-view-mixin/actions/workflows/testing.yml/badge.svg
    :target: https://github.com/frankhood/django-response-view-mixin/actions/workflows/testing.yml

.. image:: https://codecov.io/gh/frankhood/django-response-mixin-view/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/frankhood/django-response-mixin-view

Your project description goes here

Documentation
-------------

The full documentation is at https://django-response-view-mixin.readthedocs.io/.

Quickstart
----------

Install Django-response-view-mixin::

    pip install django-response-view-mixin

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'response_view_mixin',
        ...
    )


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
