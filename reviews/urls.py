"""URL Patterns"""
from django.urls import path
from . import views
#

urlpatterns = [
    path(
        "reviews/<int:pk>/delete/",
        views.ReviewDeleteView.as_view(),
        name="delete-review"),
    path(
        "review/<int:pk>/edit/",
        views.ReviewEditView.as_view(),
        name="edit-review"),
]
