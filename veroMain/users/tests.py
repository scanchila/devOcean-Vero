from django.test import TestCase

from django.contrib.auth.models import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Test",password = "Test123", email="test@test.com")

    def test_exist(self):
        user = User.objects.get(username="Test")
