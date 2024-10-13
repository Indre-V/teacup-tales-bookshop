"""Imports for test models"""
from decimal import Decimal
from datetime import timedelta
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product, Category, Genre, Author
from profiles.models import UserProfile
from coupons.models import Coupon
from checkout.models import Order, OrderLineItem


# pylint: disable=locally-disabled, no-member
# pylint: disable=locally-disabled, unused-variable


class OrderModelTest(TestCase):
    """
    Tests for the Order model.
    """

    def setUp(self):
        """
        Set up test data, including a user profile, product, and coupon.
        """
        self.user = User.objects.create_user(
            username='testuser', password='testpass123')
        self.user_profile, created = UserProfile.objects.get_or_create(
            user=self.user)

        self.category = Category.objects.create(name="Fiction")
        self.genre = Genre.objects.create(
            name="Mystery", category=self.category)
        self.author = Author.objects.create(
            name="John Doe", bio="A test author")
        self.product = Product.objects.create(
            title="Test Product",
            genre=self.genre,
            description="Test description",
            isbn="1234567890123",
            publisher="Test Publisher",
            date_published="2022-01-01",
            stock_amount=10,
            price=Decimal("20.00")
        )
        self.product.author.add(self.author)

        self.coupon = Coupon.objects.create(
            code="DISCOUNT10",
            discount_type="percentage",
            discount_value=10,
            valid_from=timezone.now() - timedelta(days=1),
            valid_until=timezone.now() + timedelta(days=30)
        )

        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            country="IE",
            town_or_city="Dublin",
            street_address1="123 Main St",
            postcode="12345",
            coupon=self.coupon,
            original_bag="",
            stripe_pid="test_pid"
        )


class OrderLineItemModelTest(TestCase):
    """
    Tests for the OrderLineItem model.
    """

    def setUp(self):
        """
        Set up test data for the order line item.
        """

        self.user = User.objects.create_user(
            username='testuser', password='testpass123')
        self.user_profile, created = UserProfile.objects.get_or_create(
            user=self.user)

        self.category = Category.objects.create(name="Fiction")
        self.genre = Genre.objects.create(
            name="Mystery", category=self.category)
        self.author = Author.objects.create(
            name="John Doe", bio="A test author")
        self.product = Product.objects.create(
            title="Test Product",
            genre=self.genre,
            description="Test description",
            isbn="1234567890123",
            publisher="Test Publisher",
            date_published="2022-01-01",
            stock_amount=10,
            price=Decimal("20.00"),
            sale_price=Decimal("15.00")
        )
        self.product.author.add(self.author)

        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            country="IE",
            town_or_city="Dublin",
            street_address1="123 Main St",
            postcode="12345",
            original_bag="",
            stripe_pid="test_pid"
        )

    def test_line_item_total_with_sale_price(self):
        """
        Test the line item total calculation with sale price.
        """
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2
        )
        line_item.save()
        self.assertEqual(line_item.lineitem_total, Decimal("30.00"))

    def test_line_item_total_without_sale_price(self):
        """
        Test the line item total calculation without sale price.
        """
        self.product.sale_price = None
        self.product.save()
        line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2
        )
        line_item.save()
        self.assertEqual(line_item.lineitem_total, Decimal("40.00"))
