from django.shortcuts import render
from rest_framework import generics, status
from .models import Book, Order, OrderItem
from .serializers import BookSerializer, RevenueSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, F
import datetime

# class BookEntryCreate(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# class OrderDetailView(generics.RetrieveAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

class OrderItemView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class RevenueView(APIView):
    def get(self, request):

        start_date = request.GET.get('start_date')
        end_date = request.GET.get("end_date")

        if not start_date or not end_date:
            return Response({"error": 'Please enter start date and end date'}, status=status.HTTP_400_BAD_REQUEST)
        
        print("Filter conditions")
        print("start date:", start_date)
        print("end date:", end_date)

        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

        except ValueError:
            return Response({"error: Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
        
        completed_orders = Order.objects.filter(status = "completed", order_date__range=[start_date, end_date])

        print(Sum('orderitem__quantity'))

        print(Sum('orderitem__book_price'))

        total_revenue = completed_orders.aggregate(total_revenue=Sum(F('orderitem__quantity') * F('orderitem__book_price')))["total_revenue"] or 0

        print("Completed Orders:", completed_orders)

        print("Total Revenue:", total_revenue)

        data={'total_revenue': total_revenue}

        print(data)

        serializer = RevenueSerializer(data)
        print("Serializer output:", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)




