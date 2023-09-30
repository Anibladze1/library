from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserRegistrationTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('register')
        self.email = "testuser@example.com"
        self.password = "strong_password_123"
        self.location = "Testland"

    def test_register_user(self):

        response = self.client.post(self.url, {
            'email': self.email,
            'password': self.password,
            'location': self.location,
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.get().email, self.email)


class UserLoginTestCase(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com", password="test_password")
        self.url = reverse('login')

    def test_valid_login(self):
        response = self.client.post(self.url, {
            'email': 'testuser@example.com',
            'password': 'test_password'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access_token' in response.data)

    def test_invalid_login(self):
        response = self.client.post(self.url, {
            'email': 'testuser@example.com',
            'password': 'wrong_password'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com", password="test_password")
        self.url = reverse('logout')
        self.login_url = reverse('login')
        login_resp = self.client.post(self.login_url, {
            'email': 'testuser@example.com',
            'password': 'test_password'
        }, format='json')
        self.token = login_resp.data['access_token']

    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTestCase(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="testuser@example.com", password="test_password")
        self.superuser = get_user_model().objects.create_superuser(
            email="admin@example.com", password="admin_password")
        self.url = reverse('delete-user', args=[self.user.id])
        self.login_url = reverse('login')
        login_resp = self.client.post(self.login_url, {
            'email': 'admin@example.com',
            'password': 'admin_password'
        }, format='json')
        self.token = login_resp.data['access_token']

    def test_delete_user(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(get_user_model().objects.filter(id=self.user.id).exists())


