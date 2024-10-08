"""Imports for Forms tests"""
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from products.models import Category, Genre, Author
from checkout.models import Order
from stock_admin.forms import (
    ProductForm,
    CategoryForm,
    GenreForm,
    AuthorForm,
    OrderStatusForm,
    CouponForm
)

# pylint: disable=locally-disabled, no-member

class TestProductForm(TestCase):
    """
    Test suite for the ProductForm.
    """

    def setUp(self):
        """
        Set up initial data for testing the ProductForm.
        """
        self.category = Category.objects.create(name="Fiction")
        self.genre = Genre.objects.create(name="Mystery", category=self.category)
        self.author = Author.objects.create(name="John Doe", bio="An author of great renown.")

    def test_product_form_valid_data(self):
        """
        Test if the form is valid with correct data.
        """
        form_data = {
            'title': 'Test Product',
            'genre': self.genre.id,
            'description': 'A great book',
            'isbn': '1234567890123',
            'publisher': 'Some Publisher',
            'date_published': timezone.now().date(),
            'stock_amount': 10,
            'price': Decimal('19.99'),
            'author': [self.author.id],
            'type': '1'
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_product_form_invalid_date_published(self):
        """
        Test if the form is invalid when the publication date is in the future.
        """
        future_date = timezone.now().date() + timedelta(days=10)
        form_data = {
            'title': 'Test Product',
            'genre': self.genre.id,
            'description': 'A great book',
            'isbn': '1234567890123',
            'publisher': 'Some Publisher',
            'date_published': future_date,  # future date
            'stock_amount': 10,
            'price': Decimal('19.99'),
            'author': [self.author.id]
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_published', form.errors)
        self.assertEqual(form.errors['date_published'], ["Date published cannot be in the future."])


class TestCategoryForm(TestCase):
    """
    Test suite for the CategoryForm.
    """

    def test_category_form_valid(self):
        """
        Test if the form is valid with correct data.
        """
        form_data = {'name': 'Fiction'}
        form = CategoryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_category_form_blank_data(self):
        """
        Test if the form is invalid with blank data.
        """
        form = CategoryForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertIn('name', form.errors)


class TestGenreForm(TestCase):
    """
    Test suite for the GenreForm.
    """

    def setUp(self):
        """
        Set up initial data for testing the GenreForm.
        """
        self.category = Category.objects.create(name="Fiction")

    def test_genre_form_valid(self):
        """
        Test if the form is valid with correct data.
        """
        form_data = {
            'name': 'Mystery',
            'category': self.category.id
        }
        form = GenreForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_genre_form_invalid_blank(self):
        """
        Test if the form is invalid with blank data.
        """
        form = GenreForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('category', form.errors)


class TestAuthorForm(TestCase):
    """
    Test suite for the AuthorForm.
    """

    def test_author_form_valid(self):
        """
        Test if the form is valid with correct data.
        """
        form_data = {
            'name': 'John Doe',
            'bio': 'An author of great renown.'
        }
        form = AuthorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_author_form_blank_data(self):
        """
        Test if the form is invalid with blank data.
        """
        form = AuthorForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('bio', form.errors)


class TestCouponForm(TestCase):
    """
    Test suite for the CouponForm.
    """

    def setUp(self):
        """
        Set up initial data for testing the CouponForm.
        """
        self.now = timezone.now()
        self.valid_from = self.now
        self.valid_to = self.now + timedelta(days=1)

    def test_coupon_form_valid(self):
        """
        Test if the form is valid with correct data.
        """
        form_data = {
            'code': 'DISCOUNT10',
            'valid_from': self.valid_from.strftime('%Y-%m-%dT%H:%M'),
            'valid_to': (self.now + timedelta(days=1)).strftime('%Y-%m-%dT%H:%M'),
            'discount_type': 'percentage',
            'discount_value': 10,
            'active': True,
            'is_used': False
        }
        form = CouponForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_coupon_form_invalid_date(self):
        """
        Test if the form rejects past valid_to dates.
        """
        form_data = {
            'code': 'DISCOUNT10',
            'valid_from': self.valid_from.strftime('%Y-%m-%dT%H:%M'),
            'valid_to': (self.now - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M'),
            'discount_type': 'percent',
            'discount_value': 10,
            'active': True,
            'is_used': False
        }
        form = CouponForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('valid_to', form.errors)
        self.assertEqual(form.errors['valid_to'], ['The "Valid To" date cannot be in the past.'])


class TestOrderStatusForm(TestCase):
    """
    Test suite for the OrderStatusForm.
    """

    def setUp(self):
        """
        Set up initial data for testing the OrderStatusForm.
        """
        self.order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            country="Ireland",
            town_or_city="Dublin",
            street_address1="123 Main St",
            postcode="12345",
            status="pending"
        )

    def test_order_status_form_valid(self):
        """
        Test if the form is valid with a correct status.
        """
        form_data = {'status': 'shipped'}
        form = OrderStatusForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_order_status_form_blank(self):
        """
        Test if the form rejects a blank status.
        """
        form_data = {'status': ''}
        form = OrderStatusForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors)

    def test_order_status_form_invalid_status(self):
        """
        Test if the form rejects an invalid status.
        """
        form_data = {'status': 'non-existent-status'}
        form = OrderStatusForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors)
