"""Imports for Views page"""
import requests
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from products.models import Product, Author
from .forms import ProductForm


class AdminDashboardView(LoginRequiredMixin, ListView):
    """
    Display all products in the admin dashboard with pagination.
    """
    model = Product
    template_name = 'stock-admin/dashboard.html'
    context_object_name = 'products'
    paginate_by = 10  # Number of products per page

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the context
        context = super().get_context_data(**kwargs)
        
        # Fetch authors for the 'Add Product' form
        context['authors'] = Author.objects.all()

        return context



class AddProductView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    View for adding a new product.
    """
    model = Product
    form_class = ProductForm
    template_name = 'stock-admin/add-product.html'

    def test_func(self):
        """
        Ensure only superusers can access this view.
        """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """
        If the form is valid, save the product and redirect.
        """
        product = form.save()
        messages.success(self.request, 'Successfully added product!')
        return redirect('product_detail', args=[product.id])

    def form_invalid(self, form):
        """
        If the form is invalid, show an error message.
        """
        messages.error(self.request, 'Failed to add product. Please ensure the form is valid.')
        return super().form_invalid(form)


class DeleteProductView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """
    Delete products by superuser
    """
    model = Product
    template_name = "stock-admin/delete-modal.html"
    success_message = "Product removed successfully"
    success_url = reverse_lazy("home")

    def test_func(self):
        """
        Ensure that only the admin can delete products.
        """
        return self.request.user.is_superuser

    def get_success_url(self):
        """
        Redirect to the HTTP referrer if available,
        otherwise use the default success URL.
        """
        referrer = self.request.META.get('HTTP_REFERER')
        if referrer:
            try:
                response = requests.head(referrer, timeout=2)
                response.raise_for_status()
                return referrer
            except requests.RequestException:
                pass
        return self.success_url


class EditProductView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    View for editing an existing product.
    """
    model = Product
    form_class = ProductForm
    template_name = 'stock-admin/edit-product.html'
    success_message = "Product updated successfully"

    def test_func(self):
        """
        Ensure only superusers can access this view.
        """
        return self.request.user.is_superuser

    def form_valid(self, form):
        """
        If the form is valid, save the updated product and redirect.
        """
        product = form.save()
        messages.success(self.request, 'Successfully updated product!')
        return redirect('home')

    def form_invalid(self, form):
        """
        If the form is invalid, show an error message.
        """
        messages.error(self.request, 'Failed to update product. Please ensure the form is valid.')
        return super().form_invalid(form)

    def get_success_url(self):
        """
        Redirect to the product detail page after successful edit.
        """
        return reverse_lazy('home', args=[self.object.id])
