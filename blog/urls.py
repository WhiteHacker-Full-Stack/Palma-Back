from django.urls import path
from .views import *


urlpatterns = [
    path('productListCreate/', ProductListCreate.as_view()),
    path('incomeLisCreate/',IncomeListCreate.as_view() ),
    path('ExpenseListCreate/', ExpenseListCreate.as_view()),
    path('CategoryListSearch/<int:id>', CategoryListSearch.as_view()),
    path('PasswordSearchView/<slug:slug>', PasswordSearchView.as_view()),
    path('IncomeSearchDateView/', IncomeSearchDateView.as_view()),
    path('ExpenseSearchDate/', ExpenseSearchDate.as_view()),

# 👉------------------------------RetrieveUpdateDestroyAPIView------------------------------👈

    path('productRetrieveUpdateDestroy/<int:pk>', ProductRetrieveUpdateDestroy.as_view()),
    path('incomeRetrieveUpdateDestroy/<int:pk>', IncomeRetrieveUpdateDestroy.as_view()),
    path('expenseRetrieveUpdateDestroy/<int:pk>', ExpenseRetrieveUpdateDestroy.as_view()),
    path('categoryRetrieveUpdateDestroy/<int:pk>', CategoryRetrieveUpdateDestroy.as_view()),
    path('employeeRetrieveUpdateDestroy/<int:pk>', EmployeeRetrieveUpdateDestroy.as_view()),

# 👉------------------------------RetrieveUpdateDestroyAPIView end------------------------------👈







]