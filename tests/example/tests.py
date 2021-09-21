#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-response-mixin-view
------------

Tests for `django-session-mixin-view` models module.
"""
from pathlib import Path
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from tests.example.models import Example
from tests.example.views import ExamplePDFAPIView, ExampleTXTAPIView, ExampleFileAPIView, ExampleCSVAPIView


class TestExamplePDFAPIViewMixin(APITestCase):
    # =============================================
    # ./manage.py test tests.example.tests.TestExamplePDFAPIViewMixin
    # =============================================

    def setUp(self):
        self.item = Example.objects.create()
        self.client = APIClient()
        self.request = APIRequestFactory()

    def test_render_to_response(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExamplePDFAPIViewMixin.test_render_to_response
        # =============================================
        file_name = 'file_test.pdf'
        file_path = Path(f"tests/static/uploads/pdf/{file_name}").absolute()
        SimpleUploadedFile(
            name="file_test.pdf",
            content=open(file_path, "rb").read(),
            content_type='application/pdf'
        )
        response = self.client.get('/tests/api/example-pdf-response/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'inline;filename=%s' % file_name)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertEqual(response.content, open(file_path, "rb").read())

    def test_get_file_dir(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExamplePDFAPIViewMixin.test_get_file_dir
        # =============================================
        file_path = Path(f"tests/static/uploads/pdf/").absolute()
        request = self.request.get('/tests/api/example-pdf-response/')
        example_pdf_api_view = ExamplePDFAPIView()
        example_pdf_api_view.request = request
        self.assertEqual(example_pdf_api_view.get_file_dir(), str(file_path))

    def test_get_file_name(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExamplePDFAPIViewMixin.test_get_file_name
        # =============================================
        request = self.request.get('/tests/api/example-pdf-response/')
        example_pdf_api_view = ExamplePDFAPIView()
        example_pdf_api_view.setup(request)
        self.assertEqual(example_pdf_api_view.get_file_name(), "file_test.pdf")



class TestExampleTXTAPIViewMixin(APITestCase):
    # =============================================
    # ./manage.py test tests.example.tests.TestExampleTXTAPIViewMixin
    # =============================================

    def setUp(self):
        self.client = APIClient()
        self.request = APIRequestFactory()

    def test_render_to_response(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExampleTXTAPIViewMixin.test_render_to_response
        # =============================================
        file_name = "file_test.txt"
        response = self.client.get("/tests/api/example-txt-response/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="%s"' % file_name)
        self.assertEqual(response['Content-Type'], 'text/plain')

    def test_get_file_name(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExamplePDFAPIViewMixin.test_get_file_name
        # =============================================
        request = self.request.get("/tests/api/example-txt-response/")
        example_txt_api_view = ExampleTXTAPIView()
        example_txt_api_view.setup(request)
        file_name = example_txt_api_view.get_file_name()
        self.assertEqual("file_test.txt", file_name)

    def test_get_file_mimetype(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExampleTXTAPIViewMixin.test_get_file_mimetype
        # =============================================
        request = self.request.get("/tests/api/example-txt-response/")
        example_txt_api_view = ExampleTXTAPIView()
        example_txt_api_view.setup(request)
        file_mimetype = example_txt_api_view.get_file_mimetype()
        self.assertEqual("text/plain", file_mimetype)

    # =============================================
    # ./manage.py test tests.example.tests.TestExampleTXTAPIViewMixin.test_build_response
    # =============================================
    def test_build_response(self):
        request = self.request.get("/tests/api/example-txt-response/")
        example_txt_api_view = ExampleTXTAPIView()
        response = example_txt_api_view.as_view()(request)

        build_response = example_txt_api_view.build_response(response, context={
            "rows": [["lorem ipsum", "lorem ipsum", "lorem ipsum"]]
        })
        self.assertEqual(build_response.status_code, 200)
        self.assertEqual(response.content, b"['lorem ipsum', 'lorem ipsum', 'lorem ipsum']\n")



class TestExampleCSVAPIViewMixin(APITestCase):
    # =============================================
    # ./manage.py test tests.example.tests.TestExampleCSVAPIViewMixin
    # =============================================

    def setUp(self):
        self.client = APIClient()
        self.request = APIRequestFactory()

    # =============================================
    # ./manage.py test tests.example.tests.TestExampleCSVAPIViewMixin.test_render_to_response
    # =============================================
    def test_render_to_response(self):
        file_name = "file_test.csv"

        response = self.client.get('/tests/api/example-csv-response/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="%s"' % file_name)
        self.assertEqual(response['Content-Type'], 'text/csv')

    # =============================================
    # ./manage.py test tests.example.tests.TestExampleCSVAPIViewMixin.test_build_response
    # =============================================
    def test_build_response(self):
        request = self.request.get('/tests/api/example-csv-response/')
        example_csv_api_view = ExampleCSVAPIView()
        response = example_csv_api_view.as_view()(request)

        build_response = example_csv_api_view.build_response(response, context={
            "rows": [["lorem ipsum", "lorem ipsum", "lorem ipsum"]]
        })
        self.assertEqual(build_response.status_code, 200)
        self.assertEqual(response.content, b"b'lorem ipsum';b'lorem ipsum';b'lorem ipsum'\r\n")


class TestExampleFileAPIViewMixin(APITestCase):
    # =============================================
    # ./manage.py test tests.example.tests.TestExampleFileAPIViewMixin
    # =============================================
    def setUp(self):
        self.client = APIClient()
        self.request = APIRequestFactory()

    def test_render_to_response(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExampleFileAPIViewMixin.test_render_to_response
        # =============================================
        file_name = "git.jpg"
        file_path = Path(f"tests/static/uploads/test_images/{file_name}").absolute()
        SimpleUploadedFile(
            name=file_name,
            content=open(file_path, "rb").read(),
            content_type='image/jpg'
        )
        request = self.request.get('/tests/api/example-file-response/')
        example_api_file_view = ExampleFileAPIView()
        response = example_api_file_view.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], f'attachment; filename="{file_name}"')
        self.assertEqual(response['Content-Type'], 'image/jpeg')

    def test_get_file_docroot(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExampleFileAPIViewMixin.test_get_file_docroot
        # =============================================
        request = self.request.get('/tests/api/example-file-response/')
        example_api_file_view = ExampleFileAPIView()
        example_api_file_view.setup(request)

    def test_get_file_path(self):
        # =============================================
        # ./manage.py test tests.example.tests.TestExampleFileAPIViewMixin.test_get_file_path
        # =============================================
        file_path = Path('uploads/test_images/git.jpg')
        request = self.request.get('/tests/api/example-file-response/')
        example_api_file_view = ExampleFileAPIView()
        example_api_file_view.setup(request)
        self.assertEqual(example_api_file_view.get_file_path(), str(file_path))

