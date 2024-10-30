from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Operator)
admin.site.register(Employee)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(SearchDate)

