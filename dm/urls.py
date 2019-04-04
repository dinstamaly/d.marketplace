"""dm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from checkout.views import CheckoutTestView, CheckoutAjaxView
from dashboard.views import DashboardView
from products.views import UserLibraryListView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('test/', CheckoutTestView.as_view(), name='test'),
    path('checkout/', CheckoutAjaxView.as_view(), name='checkout'),
    path('admin/', admin.site.urls),
    path('products/', include(("products.urls", "products"), namespace='products')),
    path('seller/', include(("sellers.urls", "sellers"), namespace='sellers')),
    path('tags/', include(("tags.urls", "tags"), namespace='tags')),
    path('library/', UserLibraryListView.as_view(), name='library'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
