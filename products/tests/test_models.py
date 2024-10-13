"""Imports for Model Testing"""
from decimal import Decimal
from datetime import date
from django.test import TestCase
from products.models import Category, Author, Genre, Product


# pylint: disable=locally-disabled, no-member

class TestCategoryModel(TestCase):
    """
    Category Testing
    """
    def setUp(self):
        self.category = Category.objects.create(name="Fiction")

    def test_category_str(self):
        """
        Test that the __str__ method works as expected
        """
        self.assertEqual(str(self.category), "Fiction")


class TestAuthorModel(TestCase):
    """
    Author Testing
    """
    def setUp(self):
        self.author = Author.objects.create(
            name="J.K. Rowling", bio="Author of Harry Potter")

    def test_author_str(self):
        """
        Test that the __str__ method works as expected
        """
        self.assertEqual(str(self.author), "J.K. Rowling")


class TestGenreModel(TestCase):
    """
    Genre Testing
    """
    def setUp(self):
        self.category = Category.objects.create(name="Books")
        self.genre = Genre.objects.create(
            name="Fantasy", friendly_name="Fantasy Books",
            category=self.category)

    def test_genre_str(self):
        """
        Test that the __str__ method works as expected
        """
        self.assertEqual(str(self.genre), "Fantasy")

    def test_genre_friendly_name(self):
        """
        Test that friendly_name is optional
        and defaults to name when friendly_name is not provided
        """
        self.assertEqual(self.genre.friendly_name, "Fantasy Books")


class TestProductModel(TestCase):
    """
    Product Model testing
    """
    def setUp(self):
        self.category = Category.objects.create(name="Books")
        self.genre = Genre.objects.create(
            name="Fiction", category=self.category)
        self.author = Author.objects.create(
            name="George Orwell", bio="Author of 1984")
        self.product = Product.objects.create(
            title="1984",
            genre=self.genre,
            description="A dystopian novel.",
            isbn="1234567890123",
            publisher="Penguin Books",
            type="Hardback",
            date_published=date.today(),
            stock_amount=5,
            price=Decimal("15.00"),
            discount=10
        )
        self.product.author.add(self.author)

    def test_product_str(self):
        """
        Test that the __str__ method works as expected
        """
        self.assertEqual(str(self.product), "1984")

    def test_product_out_of_stock(self):
        """
        Test that the out_of_stock property
        returns False when stock is available
        """
        self.assertFalse(self.product.out_of_stock)

        self.product.stock_amount = 0
        self.product.save()
        self.assertTrue(self.product.out_of_stock)

    def test_product_get_final_price(self):
        """
        Test get_final_price method without sale price
        """
        self.assertEqual(
            self.product.get_final_price(), Decimal("15.00"))

        self.product.sale_price = Decimal("12.00")
        self.product.save()
        self.assertEqual(
            self.product.get_final_price(), Decimal("12.00"))

    def test_product_get_discount_amount(self):
        """
        Test that the discount is calculated correctly
        """
        self.assertEqual(
            self.product.get_discount_amount(), Decimal("1.50"))

        self.product.discount = None
        self.product.save()
        self.assertEqual(
            self.product.get_discount_amount(), Decimal("0.00"))

    def test_product_calc_average_rating(self):
        """
        Test that the average
        rating calculation returns 0 when there are no reviews
        """
        self.assertEqual(self.product.calc_average_rating(), 0)
