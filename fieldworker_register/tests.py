from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.response import Response

from .models import Fieldworker
from .serializers import FieldworkerSerializer

# Create your tests here.
class RegistrationTestCase(APITestCase):
    def test_post(self):
        data = {'first_name':'abc','last_name':'abc','function':'Other'}
        response = self.client.post("/fieldworker/apifieldworker/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	
    def test_get(self):
        data = {'first_name':'abc','last_name':'abc','function':'Other'}
        response = self.client.get("/fieldworker/apifieldworker/",data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
