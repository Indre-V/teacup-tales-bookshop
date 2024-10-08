"""Views Tests imports"""
from decimal import Decimal
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from django.contrib.messages import get_messages
from products.models import Product


# pylint: disable=locally-disabled, no-member


class CartViewsTest(TestCase):
    """
    Cart Views Tests
    """

    def setUp(self):
        """
        Set up test data including products with stock and session.
        """
        self.product = Product.objects.create(
            title="Test Product",
            description="Test Description",
            isbn="1234567890",
            price=Decimal('10.00'),
            stock_amount=10,
            date_published=timezone.now(),
        )

        self.product2 = Product.objects.create(
            title="Second Product",
            description="Another Description",
            isbn="9876543210",
            price=Decimal('20.00'),
            stock_amount=5,
            date_published=timezone.now(),
        )
        self.client.session['cart'] = {}

    def test_add_to_cart_stock_error(self):
        """
        Test adding more products than available stock.
        """
        response = self.client.post(reverse('add-to-cart', args=[self.product.id]), {
            'quantity': 15,
            'redirect_url': '/',
        })
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)], self.product.stock_amount)
        messages = list(get_messages(response.wsgi_request))
        self.assertIn('Error: Test Product has only 10 units left.', str(messages[0]))

    def test_adjust_qty(self):
        """
        Test adjusting the quantity of a product in the cart.
        """
        response = self.client.post(reverse('change-quantity', args=[self.product.id]), {
            'quantity': 5,
        })
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)], 5)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Updated Test Product quantity to 5.')

    def test_adjust_qty_above_stock(self):
        """
        Test adjusting the quantity above available stock.
        """
        response = self.client.post(reverse('change-quantity', args=[self.product.id]), {
            'quantity': 15,
        })
        cart = self.client.session.get('cart', {})
        self.assertEqual(cart[str(self.product.id)], self.product.stock_amount)
        messages = list(get_messages(response.wsgi_request))
        self.assertIn(f'Error: You cannot add more than {self.product.stock_amount} units',
                      str(messages[0]))

    def test_remove_from_cart(self):
        """
        Test removing a product from the cart.
        """
        session = self.client.session
        session['cart'] = {str(self.product.id): 1}
        session.save()

        response = self.client.post(reverse('remove-from-cart', args=[self.product.id]))
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn(f'Removed {self.product.title} from your cart', messages)

        cart = self.client.session.get('cart', {})
        self.assertNotIn(str(self.product.id), cart)
