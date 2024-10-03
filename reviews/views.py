"""Views Imports """
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review
from .forms import ReviewProductForm


class ReviewEditView(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, UpdateView):

    """
    This view is used to allow logged-in users
    and admin to update their own reviews
    """
    model = Review
    form_class = ReviewProductForm
    template_name = "reviews/edit-review.html"
    success_message = "Review updated successfully"

    def test_func(self):
        """
        Ensure that only the review author or admin can edit the review.
        """
        review = self.get_object()
        return (
            self.request.user == review.user or
            self.request.user.is_superuser
        )

    def get_success_url(self):
        """
        After the review is updated, redirect to the product detail page.
        """

        return reverse('product-detail', kwargs={'pk': self.object.product.pk})


class ReviewDeleteView(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, DeleteView):

    """
    This view is used to allow logged in users to delete their own reviews
    """
    model = Review
    template_name = "reviews/delete-review.html"
    success_message = "Review removed successfully"

    def test_func(self):
        """
        Ensure that only the review author or admin can delete the reviews.
        """
        review = self.get_object()
        return (
            self.request.user == review.user or
            self.request.user.is_superuser
        )

    def get_success_url(self):
        """
        Redirect to the HTTP referrer if available and valid,
        otherwise use the default success URL.
        """
        referrer = self.request.META.get('HTTP_REFERER')
        if referrer:
            if self.request.get_host() in referrer:
                return referrer
        return self.success_url
