from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):

    def setUp(self):
        self.user_data = {
            'name': 'heyjay',
            'email': 'heyjay@gmail.com',
            'city': 'raipur',
            'state': 'cg',
            'zip_code': 495001
        }
        self.response = self.client.post(reverse('user-list'), self.user_data, format='json')

    def test_can_create_user(self):
        """
        Ensure we can create a new user object.
        """
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'heyjay')

    def test_can_read_user_list(self):
        """
        Ensure we can read all user objects
        """
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        """
        Ensure we can read a particular user details
        """
        id = User.objects.get().id
        response = self.client.get(reverse('user-detail', args=[id]))
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_user(self):
        """
        Ensure we can update a user with given data
        """
        id = User.objects.get().id
        test_data = {
            'name': 'teyhey',
            'email': 'teyhey@gmail.com',
            'city': 'raipur',
            'state': 'cg',
            'zip_code': 495001
        }
        response = self.client.put(reverse('user-detail', args=[id]), test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_user(self):
        """
        Ensure we can read all user objects
        """
        id = User.objects.get().id
        response = self.client.delete(reverse('user-detail', args=[id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
