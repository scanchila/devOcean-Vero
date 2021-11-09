from django.test import TestCase
from .models import GroupActivity
from django.contrib.auth.models import User
# Create your tests here.
class GroupActivityTestCase(TestCase):
    def setUp(self):
        user = User(username="TestGroupActivity", email="test@test.com",password="Test123")
        user.save()
        GroupActivity.objects.create(name="Test",address = "CRA Test # 44", contact="test@test.com",
                                     date = "2021-10-24", hour="09:50PM", duration="10", type="test",
                                     creator=user, description="This is a test")

    def test_exist(self):
        g = GroupActivity.objects.get(name="Test")