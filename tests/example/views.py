import os

from pathlib import Path
# Create your views here.
from django.conf import settings
from rest_framework import generics

from django_response_mixin_view.response_mixins import TXTResponseMixin, PDFResponseMixin, \
    CSVResponseMixin, ImageResponseServeMixin, FileResponseServeMixin


class ExamplePDFAPIView(PDFResponseMixin, generics.GenericAPIView):

    def get_file_name(self):
        return 'file_test.pdf'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={})


class ExampleCSVAPIView(CSVResponseMixin, generics.GenericAPIView):

    def get_file_name(self):
        return "file_test.csv"

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={"rows": []})


class ExampleTXTAPIView(TXTResponseMixin, generics.GenericAPIView):

    def get_file_name(self):
        return "file_test.txt"

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={"rows": []})


class ExampleFileAPIView(FileResponseServeMixin, generics.GenericAPIView):

    def get_file_docroot(self, **kwargs):
        return settings.STATIC_ROOT

    def get_file_path(self, **kwargs):
        path = Path('uploads/test_images/git.jpg')
        return str(path)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(context={})
