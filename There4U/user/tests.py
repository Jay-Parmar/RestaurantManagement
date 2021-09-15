from django.http import response
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

    def test_create_bad_request(self):
        """
        Ensure the User model won't be created for bad data.
        """
        bad_data = {
            'name': 'heyjay',
            'city': 'raipur',
            'state': 'cg',
            'zip_code': 495001
        }
        response = self.client.post(reverse('user-list'), bad_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_read_user_list(self):
        """
        Ensure we can read all user objects.
        """
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        """
        Ensure we can read a particular user details.
        """
        id = User.objects.get().id
        response = self.client.get(reverse('user-detail', args=[id]))
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_non_existing_user(self):
        """
        Ensures that it raises a 404 for a non-existing user.
        """
        id = 70
        response = self.client.get(reverse('user-detail', args=[id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_update_user(self):
        """
        Ensure we can update a user with given data.
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

    def test_update_with_bad_request(self):
        """
        Ensures we cannot update user with wrong data.
        """
        id = User.objects.get().id
        test_data = {
            'name': 'teyhey',
            'city': 'raipur',
            'state': 'cg',
            'zip_code': 495001
        }
        response = self.client.put(reverse('user-detail', args=[id]), test_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_non_existing_user(self):
        """
        Ensures we cannot update a non-existing user, raises a 404 error.
        """
        id = 70
        test_data = {
            'name': 'teyhey',
            'email': 'teyheysomething@gmail.com',
            'city': 'raipur',
            'state': 'cg',
            'zip_code': 495001
        }
        response = self.client.put(reverse('user-detail', args=[id]), test_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_delete_user(self):
        """
        Ensure we can read all user objects.
        """
        id = User.objects.get().id
        response = self.client.delete(reverse('user-detail', args=[id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_non_existing_user(self):
        """
        Ensures it raises a 404 error on deleting a non-existing user.
        """
        id = 70
        response = self.client.delete(reverse('user-detail', args=[id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
