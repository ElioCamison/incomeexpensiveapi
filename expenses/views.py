from rest_framework.viewsets import ModelViewSet

from expenses.models import Category, Expense
from expenses.serializers import CategorySerializers, ExpenseSerializers


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ExpenseModelViewSet(ModelViewSet):
    serializer_class = ExpenseSerializers

    def get_queryset(self):
        return Expense.objects.select_related("category", "user").filter(user=self.request.user)

