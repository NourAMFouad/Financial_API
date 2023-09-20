from django.db import models

# importing the User model provided by Django's built-in authentication system. 
# this model represents user accounts and comes with fields like username, email, password.
#from django.contrib.auth.models import User  



# to add users 
class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the built-in User model
    user_id = models.CharField(max_length=200, unique = True ,default = None)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.user_id


class transaction(models.Model):
    
    transaction_date = models.DateTimeField()

    description = models.CharField(max_length = 255)

    amount = models.DecimalField(max_digits= 10, decimal_places = 2)
    category = models.CharField(max_length = 100)
    
    user_id = models.CharField(max_length=200, unique = False ,default = None)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_id_transaction', default=None)

   # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    CURRENCY_CHOICES = (
        ('USD', 'US Dollar (USD)'),
        ('EUR', 'Euro (EUR)'),
        ('GBP', 'British Pound (GBP)'),
    )

    currency_type = models.CharField(max_length=1000, choices=CURRENCY_CHOICES, default = 'Unknown')

    # blank = True  --> means that is optional and can be left empty
    location = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user_id
   #     return self.description + " " + self.category + " " + self.user_id + " " + self.location + " " + self.payment_method

class registration(models.Model):
    name = models.CharField(max_length = 100)
    contact = models.CharField('Phone number', max_length = 300)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length = 300, blank = True)
    