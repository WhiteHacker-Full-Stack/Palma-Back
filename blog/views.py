from itertools import product

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from unicodedata import decimal

from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.
# list => kategory boyicha qidirish kodi orqali bittasini qidirish
# create => maxsulot yaratish chiqim yaratish kirim yaratish
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OperratorListCreate(generics.ListCreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

class ProductListCreate(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class IncomeListCreate(APIView):
    def get(self, request):
        incomes = Income.objects.all()
        serializer = IncomesSerializer(incomes, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = IncomesSerializer(data=request.data)
        data = request.data

        if serializer.is_valid():
            serializer.save()
            print('hoooooooooooooooo', data)
            product_price = float(data['product_price'])
            product_name = data['productName']
            product_count = int(data['product_count'])
            product = Products.objects.get(id = product_name)
            product.count += product_count
            summa = float(product.total_cost) + product_count * product_price
            product.total_cost = summa
            product.cost_price = product_price
            percentage = product.percentage
            product.selling_price = product_price * (1+percentage/100)
            product.save()




            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ExpenseListCreate(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = (ExpenseSerializer(expenses, many=True))
        return Response(serializer.data)
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        data = request.data

        if serializer.is_valid():
            serializer.save()
            product_price = float(data['product_price'])
            product_name = data['productName']
            product_count = int(data['product_count'])
            product = Products.objects.get(id = product_name)
            product.count -= product_count
            if product.count < 0:
                malumot = {
                    "status": "failed",
                    "xatolik":"Yetarli maxsulot mavjud emas"
                }
                return Response(malumot)
            summa = float(product.total_sales) + product_count * product_price
            product.total_sales = summa
            product.save()

            return Response(serializer.data)
        else:
                return Response(serializer.errors)


class CategoryListSearch(APIView):
    def get(self, request,id):
        products = Products.objects.filter(category=id)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

class PasswordSearchView(APIView):
    def get(self, request, slug=None):

        product = Products.objects.filter(password=slug)
        serializer = ProductsSerializer(product, many=True)
        if len(serializer.data) > 0:
            return Response(serializer.data[0])
        else:
            return Response({"error": f"{slug} passwordga ega maxsulot kiritilmagan"})

class IncomeSearchDateView(APIView):
    def get(self, request):
        incomes = SearchDate.objects.all()
        serializers = []
        for x in incomes:
            serializers.append(x.json())

        return Response(serializers)


    def post(self, request):
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        products = Income.objects.filter(created_at__range=(start_date, end_date))
        serializer = IncomesSerializer(products, many=True)
        return Response(serializer.data)

class ExpenseSearchDate(APIView):
    def get(self, request):
        incomes = SearchDate.objects.all()
        serializers = []
        for x in incomes:
            serializers.append(x.json())

        return Response(serializers)

    def post(self, request):
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        products = Expense.objects.filter(created_at__range=(start_date, end_date))
        serializer = ExpenseSerializer(products, many=True)
        return Response(serializer.data)

# 👉------------------------------RetrieveUpdateDestroyAPIView------------------------------👈

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OperatorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class IncomeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomesSerializer



class ExpenseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# ��------------------------------ReportAPIView------------------------------��















