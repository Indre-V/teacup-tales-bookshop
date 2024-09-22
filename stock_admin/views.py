"""Imports for Views page"""
import requests
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from products.models import Product, Author, Genre, Category
from .forms import ProductForm, CategoryForm, GenreForm, AuthorForm

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument

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
        return redirect('product-detail', args=[product.id])

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


class ManageAuthorView(ListView):
    """
    Displays a list of authors with the option to add, edit, and delete
    authors via modals.
    """
    model = Author
    template_name = 'stock-admin/manage-author.html'
    context_object_name = 'authors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthorForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handle the addition of a new author
        if 'add_author' in request.POST:
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage-author')

        # Handle the update of an existing author
        elif 'edit_author' in request.POST:
            author = get_object_or_404(Author, pk=request.POST['author_id'])
            form = AuthorForm(request.POST, instance=author)
            if form.is_valid():
                form.save()
                return redirect('manage-author')

        # Handle the deletion of an author
        elif 'delete_author' in request.POST:
            author = get_object_or_404(Author, pk=request.POST['author_id'])
            author.delete()
            return redirect('manage-author')

        return redirect('manage-author')


class ManageCategoryView(ListView):
    """
    Displays a list of categories with the option to add, edit, and delete
    categories via modals.
    """
    model = Category
    template_name = 'stock-admin/manage-category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context

    def post(self, request, *args, **kwargs):
        # Handle the addition of a new category
        if 'add_category' in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage-category')
 

        elif 'edit_category' in request.POST:
            category = get_object_or_404(Category, pk=request.POST['category_id'])
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                return redirect('manage-category')
        
        elif 'delete_category' in request.POST:
            category = get_object_or_404(Category, pk=request.POST['category_id'])
            category.delete()
            return redirect('manage-category')

        return redirect('manage-category')

class ManageGenreView(ListView):
    """
    Displays a list of genres with the option to add, edit, and delete
    genres via modals.
    """
    model = Genre
    template_name = 'stock-admin/manage-genre.html'
    context_object_name = 'genres'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = GenreForm()  
        return context

    def post(self, request, *args, **kwargs):
        # Handle the addition of a new genre
        if 'add_genre' in request.POST:
            form = GenreForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage-genre')

        # Handle the update of an existing genre
        elif 'edit_genre' in request.POST:
            genre = get_object_or_404(Genre, pk=request.POST['genre_id'])
            form = GenreForm(request.POST, instance=genre)
            if form.is_valid():
                form.save()
                return redirect('manage-genre')

        # Handle the deletion of a genre
        elif 'delete_genre' in request.POST:
            genre = get_object_or_404(Genre, pk=request.POST['genre_id'])
            genre.delete()
            return redirect('manage-genre')

        return redirect('manage-genre')