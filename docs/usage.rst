=====
Usage
=====

To use Django-response-mixin-view in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_response_mixin_view.apps.DjangoResponseMixinViewConfig',
        ...
    )

Add Django-response-mixin-view's URL patterns:

.. code-block:: python

    from django_response_mixin_view import urls as django_response_mixin_view_urls


    urlpatterns = [
        ...
        url(r'^', include(django_response_mixin_view_urls)),
        ...
    ]
