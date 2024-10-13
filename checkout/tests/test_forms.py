"""Form testing imports"""
from django.test import TestCase
from checkout.forms import CheckoutForm


class CheckoutFormTest(TestCase):
    """
    Checkout form testing
    """

    def setUp(self):
        """
        Set up valid form data and an instance of
        an order to be used in the tests.
        """
        self.valid_data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '+12345678901',
            'country': 'IE',
            'postcode': '12345',
            'town_or_city': 'Dublin',
            'street_address1': '123 Main Street',
            'street_address2': '',
            'county': 'Dublin',
            'coupon': None,
        }

    def test_form_valid_data(self):
        """
        Test form submission with valid data.
        """
        form = CheckoutForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_phone_number(self):
        """
        Test form validation fails with an invalid phone number.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['phone_number'] = '12345678901'
        form = CheckoutForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
        self.assertEqual(form.errors[
            'phone_number'][0],
            "Phone number must start with '+' and contain only digits.")

    def test_form_empty_phone_number(self):
        """
        Test form validation fails when phone number is empty.
        """
        invalid_data = self.valid_data.copy()
        invalid_data['phone_number'] = ''
        form = CheckoutForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)
        self.assertEqual(form.errors[
            'phone_number'][0], "This field is required.")

    def test_form_email_readonly(self):
        """
        Test the email field is readonly in the form.
        """
        form = CheckoutForm()
        self.assertTrue(form.fields['email'].widget.attrs.get('readonly'))

    def test_form_field_classes_and_placeholders(self):
        """
        Test that the form fields have the correct classes and placeholders.
        """
        form = CheckoutForm()
        placeholders = {
            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        for field_name, expected_placeholder in placeholders.items():
            self.assertEqual(form.fields[field_name].widget.attrs['class'],
                             'stripe-style-input form-control')
            if form.fields[field_name].required:
                expected_placeholder += ' *'
            self.assertEqual(form.fields[field_name].
                             widget.attrs['placeholder'], expected_placeholder)

    def test_form_autofocus_on_full_name(self):
        """
        Test that the full_name field has autofocus.
        """
        form = CheckoutForm()
        self.assertTrue(form.fields['full_name'].widget.attrs.get('autofocus'))
