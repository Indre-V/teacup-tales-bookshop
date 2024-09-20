"""Views Imports """
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review
from .forms import ReviewProductForm


class ReviewEditView(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, UpdateView):

    """
    This view is used to allow logged in users
    and admin to update their own reviews
    """
    model = Review
    form_class = ReviewProductForm
    template_name = "reviews/edit-review.html"
    success_message = "Review updated successfully"

    def test_func(self):
        """
        Ensure that only the review author or admin can delete the review.
        """
        review = self.get_object()
        return (
            self.request.user == review.user or
            self.request.user.is_superuser
        )

    def get_success_url(self):
        """
        Redirect to the post detail view after a successful review edit.
        """
        return reverse_lazy("home")


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
        Redirect to the post detail view after a successful review deletion.
        """
        return reverse_lazy("home")
