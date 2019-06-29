import datetime
import json
import shutil

import requests
import responses
from PIL import Image
from django.conf import settings
from django.test import TestCase
from rest_framework import status

from .factory import ImageFactory
from .utils import datetime_convertor


class ImageUploadViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.img = ImageFactory()
        cls.img_path = f'/app{settings.MEDIA_URL}uploads/example.jpg'
        cls.url = 'http://cleverbots.ru/api/v1/upload/photo'
        cls.place = 'test/location'

    @classmethod
    def tearDownClass(cls):
        try:
            shutil.rmtree('/app/media/uploads')
        except FileNotFoundError:
            pass

    @responses.activate
    def test_validated_data(self):
        expected_data = {
            "place": ["This field is required."],
            "img": ["No file was submitted."]
        }
        responses.add(
            responses.POST,
            self.url, json=expected_data, status=status.HTTP_400_BAD_REQUEST)

        r = requests.post(self.url)

        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(r.content, expected_data)

    @responses.activate
    def test_method_post_is_required(self):
        expected_data = {"detail": "Method 'GET' not allowed."}
        responses.add(
            responses.GET,
            self.url,
            json=expected_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        r = requests.get(self.url)

        self.assertEqual(r.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertJSONEqual(r.content, expected_data)

    @responses.activate
    def test_image_uploaded(self):
        payload = {'img': self.img, 'place': self.place}
        img = Image.open(self.img_path)
        responses.add(responses.POST, self.url, status=status.HTTP_200_OK)

        r = requests.post(self.url, payload)

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertTrue(img)


class ImageFilterViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.img1 = ImageFactory(
            size=23425,
            date=datetime.datetime(2019, 5, 17, 22, 44, 23, 479995))
        cls.img2 = ImageFactory(
            size=23425,
            date=datetime.datetime(2019, 5, 17, 22, 44, 23, 479995))
        cls.url = 'http://cleverbots.ru/api/v1/upload/photo'

    @responses.activate
    def test_validated_data_date(self):
        payload = {'date': '2019-04-24T18:25:18.479995lolkek'}
        expected_data = {"date": ["Enter a valid date/time."]}
        responses.add(
            responses.GET,
            self.url, json=expected_data, status=status.HTTP_400_BAD_REQUEST)

        r = requests.get(self.url, payload)

        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(r.content, expected_data)

    @responses.activate
    def test_validated_data_size(self):
        payload = {'size': 'тесты для сильных'}
        expected_data = {"size": ["Enter a number."]}
        responses.add(
            responses.GET,
            self.url, json=expected_data, status=status.HTTP_400_BAD_REQUEST)

        r = requests.get(self.url, payload)

        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertJSONEqual(r.content, expected_data)

    @responses.activate
    def test_response_data(self):
        payload = {'size': 23425, 'date': '2019-05-17T22:44:23.479995'}
        expected_data = {
            'date': json.dumps(self.img1.date, default=datetime_convertor),
            'size': self.img1.size,
            'place': self.img1.place,
            'path_to_img': self.img1.place
        }
        responses.add(
            responses.GET,
            self.url, json=expected_data, status=status.HTTP_200_OK)

        r = requests.get(self.url, payload)

        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(r.content, expected_data)
