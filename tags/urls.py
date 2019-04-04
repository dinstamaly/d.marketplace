from django.urls import path

from .views import (
    TagDetailView,
    TagListView,
)

urlpatterns = [
    path('', TagListView.as_view(), name='list'),
    path('<slug:slug>/', TagDetailView.as_view(), name='detail'),
]
