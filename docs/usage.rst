=====
Usage
=====

To use Django Response View Mixin in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'response_view_mixin.apps.ResponseViewMixinConfig',
        ...
    )

Add Django Response View Mixin's URL patterns:

.. code-block:: python

    from response_view_mixin import urls as response_view_mixin_urls


    urlpatterns = [
        ...
        url(r'^', include(response_view_mixin_urls)),
        ...
    ]
