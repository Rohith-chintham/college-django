from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage

class ContactMessageModelTest(TestCase):
    def test_create_contact_message(self):
        message = ContactMessage.objects.create(
            name='Test User',
            email='test@example.com',
            message='This is a test message.'
        )
        self.assertEqual(message.name, 'Test User')
        self.assertEqual(ContactMessage.objects.count(), 1)

class ContactViewTest(TestCase):
    def test_contact_page_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/contact.html')

    def test_contact_form_submission(self):
        data = {
            'name': 'Alice',
            'email': 'alice@example.com',
            'message': 'Hello, this is a message.'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(name='Alice').exists())
