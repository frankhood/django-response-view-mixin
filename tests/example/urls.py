from django.urls import path

from . import views as api_views

urlpatterns = [
    path("api/example-txt-response/", api_views.ExampleTXTAPIView.as_view()),
    path("api/example-file-response/", api_views.ExampleFileAPIView.as_view()),
    path("api/example-pdf-response/", api_views.ExamplePDFAPIView.as_view()),
    path("api/example-csv-response/", api_views.ExampleCSVAPIView.as_view()),
]
