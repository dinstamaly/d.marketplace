from django.urls import path

from products.views import (
    SellerProductListView,
    ProductCreateView,
    ProductUpdateView,
)
from .views import (
    SellerDashboard,
    SellerProductDetailRedirectView,
    SellerTransactionListView,
)

urlpatterns = [
    path('', SellerDashboard.as_view(), name='dashboard'),
    path('transactions/', SellerTransactionListView.as_view(), name='transactions'),
    path('products/', SellerProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', SellerProductDetailRedirectView.as_view()),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
]
