from rest_framework import serializers

from blog.models import Category, Operator,Employee,Products,Income,Expense, SearchDate

def checkSlug(slug):
    g = 0
    for x in slug:
        if x == " ":
            g += 1
    l = slug.islower()

    if g==0 and l==True:
        return True
    else:
        return False



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__',)

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('__all__',)

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')
    def validate(self,data):
        product_name = data['name']
        if Products.objects.filter(name=product_name).exists():
            raise serializers.ValidationError("Product name already exists.")

        password = data['password']
        print('hoooooooooooooooooo', checkSlug(password))
        if Products.objects.filter(password=password).exists() or not checkSlug(password):
            raise serializers.ValidationError("Password already exists. Yoki password kichik harflarda va boshjoyi bolmasligi kerak")

        return data






class IncomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('__all__')
    def validate(self, data):
        employee = data['employee']
        product_price = data['product_price']
        product_count = data['product_count']
        product_name = data['productName']

        checkemployee = Employee.objects.get(name=employee).performance.name
        if not checkemployee == 'maxsulotkirgizuvchi':
            raise serializers.ValidationError("Only maxsulotkirgizuvchi can make incomes.")

        return data


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('__all__')

    def validate(self, data):
        employee = data['employee']
        print("hoooooo",employee)
        checkemployee = Employee.objects.get(name=employee).performance.name
        print("hoooooo",checkemployee)
        if not checkemployee == 'sotuvchi':
            print("ishladi.")
            raise serializers.ValidationError("Only sotuvchi can make expenses.")

        return data


class SearchDateSerializer(serializers.Serializer):
    class Meta:
        model = SearchDate
        fields = ('__all__')










