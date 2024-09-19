from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
    path(
        "profile/<int:pk>/delete", views.profile_delete, name="profile-delete"
    ),
]