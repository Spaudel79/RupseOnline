from django.test import TestCase
from .models import Contact

# Create your tests here.

class TestContact(TestCase):

    def setUp(self):
        self.contact = contact1= Contact.objects.create(
            full_name = "John Van",
            email = "jon@gmail.com",
            phone = 9845666777,
            subject = "My query",
            message = "test message"
        )

        self.contact = contact2 = Contact.objects.create(
            full_name="Johnw Vane",
            email="jon2@gmail.com",
            phone=9845766777,
            subject="Mys query",
            message="tesst message"
        )
        self.assertEqual(str(contact2), 'Johnw Vane')
        self.assertEqual(contact1.full_name ,"John Van")

    def test_contact_count(self):
        self.assertEqual(Contact.objects.count(),2)

    # def name_test(self):
    #     self.assertEqual(contact1.fullname ="John Van")

    # def string_test(self):
    #     self.assertEqual(str(contact2),'Johnw Vane')


