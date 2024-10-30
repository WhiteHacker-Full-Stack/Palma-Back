from django.db import models
from rest_framework.views import APIView


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Operator(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    birth_of_year = models.IntegerField()
    performance = models.ForeignKey(Operator,on_delete=models.CASCADE )
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    total_cost = models.DecimalField(max_digits=20, decimal_places=2)
    total_sales = models.DecimalField(max_digits=20, decimal_places=2)
    percentage = models.IntegerField()
    cost_price =  models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name


class Income(models.Model):
    productName = models.ForeignKey(Products, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product_count = models.IntegerField()
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.productName.name


class Expense(models.Model):
    productName = models.ForeignKey(Products, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    product_count = models.IntegerField()
    product_price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.productName.name

class SearchDate(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.start_date}'
    def json(self):
        return {
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat()
        }