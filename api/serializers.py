# Convert python object in models.py to json format so we can interact with it
from rest_framework import serializers
from .models import Book, Order, OrderItem


class BookSerializer(serializers.ModelSerializer):
    # total_rev = serializers.DecimalField(max_digits = 12, decimal_places = 2)
    class Meta:
        model = Book
        fields = ["id", "price"]

class OrderItemSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "order", "book", "quantity", "book_price"]

class OrderSerializer(serializers.ModelSerializer):
    OrderItem = OrderItemSerializer(many = True,read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'status', 'OrderItem']

class RevenueSerializer(serializers.Serializer):
    total_revenue = serializers.DecimalField(max_digits = 10, decimal_places = 2)
    