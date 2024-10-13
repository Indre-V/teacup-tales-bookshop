"""
URL configuration for teacup_tales_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import custom_400, custom_403, custom_404, custom_500


# Customize admin headers and titles
admin.site.site_header = "Teacup Tales Books Administration"
admin.site.site_title = "Teacup Tales Books Admin"
admin.site.index_title = "Welcome to Teacup Tales Books Administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('management/', include('stock_admin.urls')),
    path('cart/', include('cart.urls')),
    path('profile/', include('profiles.urls')),
    path(' ', include('reviews.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    path('checkout/', include('checkout.urls')),
    path('', include('customer_service.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = custom_400
handler403 = custom_403
handler404 = custom_404
handler500 = custom_500
