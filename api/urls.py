from django.urls import path
from . import views

urlpatterns = [
    # path("books/", views.BookEntryCreate.as_view(), name="Book-entry-create"),
    path("orders/revenue/", views.RevenueView.as_view(), name="Revenue-view"),
    path("orders/", views.OrderListView.as_view(), name='Order-list'),
    # path("orders/<int:pk>", views.OrderDetailView.as_view(), name='Order-detail'),
    path("orderitem/", views.OrderItemView.as_view(), name='Order-item')
]