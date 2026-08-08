
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class LogViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.add_log_url = reverse("logs:add_log")

    def test_add_log_page_redirects_anonymous_user(self):
        response = self.client.get(self.add_log_url)
        self.assertEqual(response.status_code, 302)

    def test_add_log_page_accessible_by_logged_in_user(self):
        # لاگین کردن کاربر فرضی
        self.client.login(username="testuser", password="password123")
        response = self.client.get(self.add_log_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "logs/add_log.html")