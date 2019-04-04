from django.urls import path
from django.views.generic.base import RedirectView
from products.views import (
    ProductCreateView,
    ProductDetailView,
    # ProductDownloadView,
    ProductListView,
    ProductUpdateView,
    ProductRatingAjaxView,
    VendorListView,
)

urlpatterns = [

    path('', ProductListView.as_view(), name='list'),
    path('vendor/', RedirectView.as_view(pattern_name='products:list'), name='vendor_list'),
    path('vendor/<vendor_name>', VendorListView.as_view(), name='vendor_detail'),
    path('ajax/rating/', ProductRatingAjaxView.as_view(), name='ajax_rating'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail_slug'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='update'),
    path('<slug:slug>/edit/', ProductUpdateView.as_view(), name='update_slug'),

]
