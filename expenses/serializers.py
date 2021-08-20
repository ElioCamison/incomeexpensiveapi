from rest_framework import serializers

from .models import Category, Expense


class CategorySerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = (
            "id",
            "user",
            "name"
        )


class ExpenseSerializers(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Expense
        fields = (
            "owner",
            "category",
            "amount",
            "date"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        user = self.context["request"].user
        self.fields["category"].queryset = user.categories.all()
