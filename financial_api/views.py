from django.shortcuts import render, redirect, get_object_or_404
from .models import transaction
from .models import UserProfile  
from .forms import transactionForm, userForm

from django.utils import timezone  # Import timezone module


# Authentication
# IsAuthentication --> to handle requests when write it in class
#from rest_framework.decorators import api_view
'''
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
'''
# CRUD - create, retrieve, update, delete, list 
# List 
def transactions_list(request):
    transactions = transaction.objects.all()

    context = {
        "transactions" : transactions
    }
    return render(request, "trans.html", context)

# create (POST)
# for creating we want to submit form 
# django include sub module to create form and submit data 
# # in app directory --> create file called forms.py 
# 
# back to views.py to use the form and create our view

# create trans_create.html file to write html forms(django replace it) and help us to submit it
# form.as_p  as a paragraph
# and go to urls.py 

### now we create the form and make user to enter the values of fileds 
# how we can make him to save the values?
# WE want to handle the submit of this form
# go to trans html file and write method = post
# write csrf 
# and create submit button
#  


#add authentication, To ensure only authenticated users can create transactions
#permission_classes = (IsAuthenticated, )

'''
api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
'''

def transaction_create(request):
    # Create an empty form
    form = transactionForm()

    if request.method == "POST":
        form = transactionForm(request.POST)
        # To show the result in the terminal, just for testing
        print(request.POST)
        if form.is_valid():
            user_id = request.POST.get('user_id')  # Assuming you have a field in the form for user_id

            # Check if the user exists in the database
            try:
                user_profile = UserProfile.objects.get(user_id=user_id)
            except UserProfile.DoesNotExist:
                # User not found, display a message and suggest registration
                context = {
                    "form": form,
                    "user_not_found": True,
                }
                return render(request, "trans_create.html", context)

            # Create and link the transaction to the user profile
            tr = form.save(commit=False)
            tr.user_profile = user_profile
            tr.save()

            return redirect("/homePage/")

    context = {
        # Don't forget to include this in the HTML template for displaying the message
        "form": form,
    }
    return render(request, "trans_create.html", context)


## retrieve function 
def trans_retrieve(request, pk):
    trans_ret = transaction.objects.get(id=pk)
    context = {
        "trans_ret": trans_ret
    }
    return render(request, "trans_retrieve.html", context)


#update and delete

def transaction_update(request, pk):
    # create empty form
   
    trans_ret = transaction.objects.get(id=pk)
    form = transactionForm(instance = trans_ret)


    if request.method == "POST":
        form = transactionForm(request.POST, instance = trans_ret)
       # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/trans_list/")
    context = {
        # donot forget to write this in html file "form"
        "form" : form
    }
    return render(request, "trans_update.html" , context) 


# to get categories 
def trans_categories(request, category):
    trans_all_category = transaction.objects.filter(category=category)
    print(trans_all_category)
    context = {
        "transactions": trans_all_category   ## Pass the filtered queryset to the template
    }
    return render(request, "trans_All_category.html", context)



# delete methods 
'''
def transaction_delete(request, pk):
    trans_to_delete = get_object_or_404(transaction, id=pk)

    if request.method == "POST":
        trans_to_delete.delete()
        return redirect("/trans_list/")

    context = {
        "trans_to_delete": trans_to_delete,
    }

    return render(request, "trans_delete.html", context)
'''

# New user registeration
# endpiont 4
def userProfile_create(request):
    # create empty form
    form = userForm()
    if request.method == "POST":
        form = userForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/homePage/")
    context = {
        # donot forget to write this in html file "form"
        "form" : form
    }
    return render(request, "user_create.html" , context) 



# List all registered users
def users_list(request):
    register_users = UserProfile.objects.all()

    context = {
        "register_users" : register_users
    }
    return render(request, "users_list.html", context)

# welcome Or Home page
# create it to redirect any function 
def homePage(request):
    register_users = UserProfile.objects.all()

    context = {
        "register_users" : register_users
    }
    return render(request, "homePage.html", context)


# endpoint 5
# retrieve transactions for user
def retrieve_all_user_trans(request, user_id):
    trans_ret = transaction.objects.filter(user_id=user_id)
    context = {
        "trans_ret": trans_ret
    }
    return render(request, "retrieve_all_user_trans.html", context)


# endpoint 6
# reports
def generate_financial_report(request, user_id):

    current_month = timezone.now().month
    current_month_transactions = transaction.objects.filter(
    transaction_date__month=current_month,
    user_id=user_id  # Filter by user_id 
    )

    # Force evaluation of the queryset by converting it to a list
    current_month_transactions_list = list(current_month_transactions)
 

    # Calculate financial summary
    total_amount = sum(transaction.amount for transaction in current_month_transactions)
    print(f"Transaction Amount: {transaction.amount}")


    context = {
        'user_id': user_id,  # Include user_id in the context
        'total_amount': total_amount 
    } 

    return render(request, "report.html", context )