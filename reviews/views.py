"""Views Imports """
from django.shortcuts import render

from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Review

class ReviewDeleteView(
        LoginRequiredMixin, UserPassesTestMixin,
        SuccessMessageMixin, DeleteView):

    """
    This view is used to allow logged in users to delete their own comments
    """
    model = Review
    template_name = "reviews/delete-comment.html"
    success_message = "Review removed successfully"

    def test_func(self):
        """
        Ensure that only the comment author or admin can delete the comment.
        """
        comment = self.get_object()
        return (
            self.request.user == comment.user or
            self.request.user.is_superuser
        )

    def get_success_url(self):
        """
        Redirect to the post detail view after a successful comment deletion.
        """
        return reverse_lazy("home")
