"""Test_Views Imports"""
from datetime import timedelta
from decimal import Decimal
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from products.models import Product, Author, Genre, Category
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem


# pylint: disable=locally-disabled, no-member


class ProductListViewTest(TestCase):
    """
    Tests for the product list view.
    """

    def setUp(self):
        """
        Set up data for the tests, creating more than 6
        products to trigger pagination.
        """
        self.category = Category.objects.create(name='Fiction')
        self.genre = Genre.objects.create(
            name='Mystery', category=self.category)
        self.author = Author.objects.create(
            name='John Doe', bio='A great author.')

        for i in range(7):
            product = Product.objects.create(
                title=f"Product {i}",
                genre=self.genre,
                description=f"Description for product {i}.",
                isbn=f"123456789012{i}",
                publisher="Test Publisher",
                date_published=timezone.now(),
                stock_amount=10,
                price=20.00 + i,
                added=timezone.now() - timedelta(days=i)
            )
            product.author.add(self.author)

    def test_pagination(self):
        """
        Test if pagination works correctly in the product list view.
        """
        response = self.client.get(reverse('all-products'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_paginated'])
        self.assertEqual(len(response.context['products']), 6)
        response = self.client.get(reverse('all-products') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products']), 1)


class ProductDetailViewTest(TestCase):
    """
    Tests for the product detail view.
    """

    def setUp(self):
        """
        Set up necessary objects for testing the product detail view.
        """
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.profile = UserProfile.objects.get_or_create(user=self.user)
        self.category = Category.objects.create(name="Fiction")
        self.genre = Genre.objects.create(
            name="Mystery", category=self.category)
        self.author = Author.objects.create(
            name="John Doe", bio="An author of great renown.")
        self.product = Product.objects.create(
            title="Test Product",
            genre=self.genre,
            description="A test product description.",
            isbn="1234567890123",
            publisher="Test Publisher",
            date_published=timezone.now(),
            stock_amount=10,
            price=19.99,
            added=timezone.now()
        )
        self.product.author.add(self.author)
        self.order = Order.objects.create(
            user_profile=self.profile,
            full_name="Test User",
            email="test@example.com",
            phone_number="123456789",
            country="Ireland",
            town_or_city="Dublin",
            street_address1="123 Street",
            postcode="D01"
        )
        self.line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1
        )


class ProductSearchViewTest(TestCase):
    """
    Tests for the product search view.
    """

    def setUp(self):
        """
        Set up the products, genres, and
        authors to test the ProductSearchView.
        """
        self.category = Category.objects.create(name='Fiction')
        self.genre = Genre.objects.create(
            name='Mystery', category=self.category)
        self.author = Author.objects.create(
            name='John Doe', bio='An author of mystery novels.')

        self.product1 = Product.objects.create(
            title="Mystery Book 1",
            genre=self.genre,
            description="A mysterious book.",
            isbn="1234567890123",
            publisher="Mystery House",
            date_published=timezone.now() - timedelta(days=5),
            stock_amount=5,
            price=15.99,
            added=timezone.now() - timedelta(days=5)
        )
        self.product1.author.add(self.author)

        self.product2 = Product.objects.create(
            title="Adventure Book 2",
            genre=self.genre,
            description="An adventurous book.",
            isbn="1234567890124",
            publisher="Adventure House",
            date_published=timezone.now() - timedelta(days=20),
            stock_amount=10,
            price=19.99,
            added=timezone.now() - timedelta(days=20)
        )
        self.product2.author.add(self.author)

    def test_search_results(self):
        """
        Test the search functionality for products.
        """
        Product.objects.create(title="Mystery Book 1",
                               price=Decimal('10.00'),
                               genre=self.genre, date_published=timezone.now())
        Product.objects.create(title="Adventure Book 2",
                               price=Decimal('15.00'),
                               genre=self.genre, date_published=timezone.now())
        Product.objects.create(title="Mystery Book 3",
                               price=Decimal('20.00'),
                               genre=self.genre, date_published=timezone.now())

        response = self.client.get(
            reverse('product-search') + '?title=Mystery')

        self.assertContains(response, 'Mystery Book 1')
        self.assertContains(response, 'Mystery Book 3')
        self.assertNotContains(response, 'Adventure Book 2')

    def test_filter_results(self):
        """
        Test that the products are correctly filtered by genre.
        """
        response = self.client.get(
            reverse('product-search') + f'?genre={self.genre.id}')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mystery Book 1')
        self.assertContains(response, 'Adventure Book 2')

    def test_sorting_results(self):
        """
        Test that the products are correctly sorted by title.
        """
        response = self.client.get(
            reverse('product-search') + '?sort_by=title_asc')
        products = response.context['products']
        self.assertEqual(products[0].title, 'Adventure Book 2')
        self.assertEqual(products[1].title, 'Mystery Book 1')

    def test_pagination(self):
        """
        Test that pagination works correctly in product search view.
        """
        for i in range(12):
            Product.objects.create(
                title=f"Product {i+1}",
                price=Decimal('10.00'),
                date_published=timezone.now(),
                genre=self.genre
            )

        response = self.client.get(
            reverse('product-search') + '?page=1')
        self.assertEqual(len(response.context['products']), 6)

        response = self.client.get(reverse(
            'product-search') + '?page=2')
        self.assertEqual(len(response.context['products']), 6)

    def test_context_data(self):
        """
        Test that the filter form is included in the context data.
        """
        response = self.client.get(reverse('product-search'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)


class SpecialOffersViewTest(TestCase):
    """
    Tests for the special offers view.
    """

    def setUp(self):
        """
        Set up products with and without
        special offers to test the special offers view.
        """
        self.product_with_sale = Product.objects.create(
            title="Product With Sale",
            price=Decimal("20.00"),
            sale_price=Decimal("15.00"),
            discount=0,
            date_published=timezone.now()
        )

        self.product_with_discount = Product.objects.create(
            title="Product With Discount",
            price=Decimal("25.00"),
            sale_price=None,
            discount=10,
            date_published=timezone.now()
        )

        self.product_without_offer = Product.objects.create(
            title="Product Without Offer",
            price=Decimal("30.00"),
            sale_price=None,
            discount=0,
            date_published=timezone.now()
        )

    def test_special_offers_view(self):
        """
        Test if the special offers
        view displays products with special offers.
        """
        response = self.client.get(reverse('special-offers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'products/special-offers.html')
        self.assertContains(response, "Product With Sale")
        self.assertContains(response, "Product With Discount")
        self.assertNotContains(response, "Product Without Offer")

    def test_sorting_in_special_offers(self):
        """
        Test sorting functionality in the special offers view.
        """
        response = self.client.get(
            reverse('special-offers') + '?sort_by=title_asc')
        self.assertEqual(response.status_code, 200)
        products = response.context['products']
        self.assertEqual(products[0].title, "Product With Discount")
        self.assertEqual(products[1].title, "Product With Sale")

        response = self.client.get(
            reverse('special-offers') + '?sort_by=title_desc')
        self.assertEqual(response.status_code, 200)
        products = response.context['products']
        self.assertEqual(products[0].title, "Product With Sale")
        self.assertEqual(products[1].title, "Product With Discount")
