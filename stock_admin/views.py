"""Imports for Views page"""
from datetime import datetime
import requests
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, TemplateView
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
from coupons.models import Coupon
from checkout.models import OrderLineItem, Order
from profiles.models import UserProfile
from products.models import Product, Author, Genre, Category
from products.mixins import SortingMixin
from products.forms import SortForm
from .forms import ProductForm, CategoryForm, GenreForm, AuthorForm, CouponForm, OrderStatusForm

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument


class ProductAdminView(LoginRequiredMixin, SortingMixin, ListView):
    """
    Display all products in the admin dashboard with sorting and pagination.
    """
    model = Product
    template_name = 'stock-admin/dashboard.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):

        queryset = super().get_queryset()

        return self.apply_sorting(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sort_form'] = SortForm(self.request.GET)

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
        return redirect('product-detail', pk=str(product.id))

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
    template_name = "stock-admin/delete-product.html"
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
        return redirect('product-detail', pk=str(product.id))

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
        """
        Handles adding new author
        """
        if 'add_author' in request.POST:
            form = AuthorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage-author')

        elif 'edit_author' in request.POST:
            author = get_object_or_404(Author, pk=request.POST['author_id'])
            form = AuthorForm(request.POST, instance=author)
            if form.is_valid():
                form.save()
                return redirect('manage-author')

        elif 'delete_author' in request.POST:
            author = get_object_or_404(Author, pk=request.POST['author_id'])
            author.delete()
            return redirect('manage-author')

        return redirect('manage-author')


class ManageCategoryView(ListView):
    """
    Categories management
    """
    model = Category
    template_name = 'stock-admin/manage-category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles categories managing
        """
        if 'add_category' in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Category added successfully.")
                return redirect('manage-category')
            else:
                categories = Category.objects.all()
                return render(request, 'stock-admin/manage-category.html', {
                    'categories': categories,
                    'form': form,
                })

        elif 'edit_category' in request.POST:
            category = get_object_or_404(Category, pk=request.POST.get('category_id'))
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid():
                form.save()
                messages.success(request, f"Category '{category.name}' updated successfully.")
                return redirect('manage-category')
            else:
                categories = Category.objects.all()
                return render(request, 'stock-admin/manage-category.html', {
                    'categories': categories,
                    'form': form,
                    'edit_category_id': category.id,
                })

        elif 'delete_category' in request.POST:
            category = get_object_or_404(Category, pk=request.POST.get('category_id'))

            if category.genre_set.exists():

                messages.error(request, f"Cannot delete category '{category.name}' because it has genres attached.")
            else:
                category.delete()
                messages.success(request, f"Category '{category.name}' has been deleted.")
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
        context['categories'] = Category.objects.all()

        genres_with_forms = []
        for genre in context['object_list']:
            genre_form = GenreForm(instance=genre)
            genres_with_forms.append((genre, genre_form))
        context['genres_with_forms'] = genres_with_forms

        return context

    def post(self, request, *args, **kwargs):
        """
        Handles adding new genre
        """
        if 'add_genre' in request.POST:
            form = GenreForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage-genre')

        elif 'edit_genre' in request.POST:
            genre = get_object_or_404(Genre, pk=request.POST.get('genre_id'))
            form = GenreForm(request.POST, instance=genre)
            if form.is_valid():
                form.save()
                messages.success(request, 'Genre updated successfully.')
                return redirect('manage-genre')
            else:
                self.object_list = self.get_queryset()
                context = self.get_context_data()
                context['edit_form'] = form
                context['edit_genre_id'] = genre.id
                return self.render_to_response(context)

        elif 'delete_genre' in request.POST:
            genre = get_object_or_404(Genre, pk=request.POST['genre_id'])
            if genre.product_set.exists():

                messages.error(request, "Cannot delete genre because it has products attached.")
            else:
                genre.delete()
                messages.success(request, "Genre deleted successfully.")
            return redirect('manage-genre')


class ManageCouponView(ListView):
    """
    Displays a list of coupons with the option to add, edit, and delete
    coupons via modals.
    """
    model = Coupon
    template_name = 'stock-admin/manage-coupon.html'
    context_object_name = 'coupons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CouponForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles adding, editing, and deleting coupons.
        """
        response_data = {'success': False}
        if 'add_coupon' in request.POST:
            form = CouponForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Coupon added successfully!')
                response_data = {'success': True}
            else:
                response_data['errors'] = form.errors

        elif 'edit_coupon' in request.POST:
            coupon = get_object_or_404(Coupon, pk=request.POST['coupon_id'])
            form = CouponForm(request.POST, instance=coupon)
            if form.is_valid():
                form.save()
                messages.success(request, 'Coupon updated successfully!')
                response_data = {'success': True}
            else:
                response_data['errors'] = form.errors
                print("Edit Coupon Form errors:", form.errors)

        elif 'delete_coupon' in request.POST:
            coupon = get_object_or_404(Coupon, pk=request.POST['coupon_id'])
            coupon.delete()
            messages.success(request, 'Coupon deleted successfully!')
            response_data = {'success': True}

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(response_data)
        else:
            return redirect('manage-coupon')


class ManageOrdersView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    Displays a list of all orders with options to update the status of each order,
    ordered by most recent first.
    """
    model = Order
    template_name = 'stock-admin/manage-orders.html'
    context_object_name = 'orders'
    paginate_by = 6

    def test_func(self):
        """
        Ensure only superusers can access this view.
        """
        return self.request.user.is_superuser

    def get_queryset(self):
        """
        Return the list of orders ordered by the most recent (descending by date).
        """
        return Order.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        """
        Add additional context such as the status form.
        """
        context = super().get_context_data(**kwargs)
        context['status_form'] = OrderStatusForm()  # Empty form for updating status
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles the update of an order's status when the form is submitted.
        """
        if 'update_status' in request.POST:
            order_id = request.POST.get('order_id')
            order = get_object_or_404(Order, id=order_id)
            form = OrderStatusForm(request.POST, instance=order)
            if form.is_valid():
                form.save()
                messages.success(request, f"Order {order.order_number} status updated successfully!")
            else:
                messages.error(request, f"Failed to update order {order.order_number} status. Please ensure the form is valid.")
        return redirect('manage-orders')


class AdminSummaryView(TemplateView):
    """
    View to display an administrative summary, including total sales, today's sales,
    new customers, and stock utilization data.
    """
    template_name = 'stock-admin/admin-summary.html'

    def get_context_data(self, **kwargs):
        """
        Summary Data
        """
        context = super().get_context_data(**kwargs)

        context['total_sales'] = Order.objects.aggregate(
            total_sales_amount=Sum('grand_total')
        )['total_sales_amount'] or 0

        context['orders_today'] = Order.objects.filter(
            date__date=datetime.today()
        ).count()

        context['total_customers'] = UserProfile.objects.count()

        context['new_customers_today'] = UserProfile.objects.filter(
            user__date_joined__date=datetime.today()
        ).count()

        context['books_in_stock'] = Product.objects.aggregate(
            total_books=Sum('stock_amount')
        )['total_books'] or 0

        context['books_sold_today'] = OrderLineItem.objects.filter(
            order__date__date=datetime.today()
        ).aggregate(total_books_sold=Sum('quantity'))['total_books_sold'] or 0

        context['todays_sales'] = Order.objects.filter(
            date__date=datetime.today()
        ).aggregate(todays_sales_amount=Sum('grand_total'))['todays_sales_amount'] or 0

        context['total_revenue'] = Order.objects.aggregate(
            total_revenue=Sum('grand_total')
        )['total_revenue'] or 0

        total_books_sold = OrderLineItem.objects.aggregate(
            total_books_sold=Sum('quantity')
        )['total_books_sold'] or 0

        total_books = Product.objects.aggregate(
            total_books=Sum('stock_amount')
        )['total_books'] or 0

        context['stock_utilization'] = (
            (total_books_sold / total_books) * 100 if total_books > 0 else 0
        )

        return context
