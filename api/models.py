from django.db import models

# Create your models here.
# class Book(models.Model):
#     price = models.DecimalField(max_digits=12, decimal_places=2)
#     order_date = models.DateField()
#     status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("completed", "Completed")])

class Book(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.price
    
class Order(models.Model):
    order_date = models.DateField()
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("completed", "Completed")])

    def __str__(self):
        return f"Order {self.id} - {self.status}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitem')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    book_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"
