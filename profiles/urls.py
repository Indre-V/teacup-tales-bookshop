from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
    path(
        "profile/<int:pk>/delete", views.profile_delete, name="profile-delete"
    ),
    path(
        'profile/wishlist_add/<str:pk>/',
        views.add_remove_wishlist_items,
        name="manage-wishlist",
    ),
    path('profile/<int:pk>/wishlist/', views.my_wishlist, name='my-wishlist'),
]
