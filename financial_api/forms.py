from django.forms import ModelForm
from .models import transaction
from .models import UserProfile  

class transactionForm(ModelForm):
    class Meta:
        model = transaction
        fields = [
            "transaction_date",
            "description",
            "amount",
            "category",
            "user_id",
            "currency_type",
            "location",
            "payment_method"
        ]

class userForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "user_id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "password"
        ]