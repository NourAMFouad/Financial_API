
from django.contrib import admin
from django.urls import path, include

from financial_api.views import transactions_list, transaction_create, trans_retrieve, transaction_update, trans_categories, userProfile_create, users_list, homePage, retrieve_all_user_trans, generate_financial_report #, transaction_delete

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trans_list/', transactions_list ),
    path('trans_create/', transaction_create),
    path('trans_retrieve/<pk>/', trans_retrieve),
    path('trans_update/<pk>/edit/', transaction_update),
    path('list_all_categories/<str:category>/', trans_categories),
    path('api/token/',obtain_auth_token ),
    path('user_create/', userProfile_create),
    path('api/users/', users_list),
    path('api/users/<str:user_id>/transactions/', retrieve_all_user_trans),
    path('api/reports/<str:user_id>/', generate_financial_report),
    path('homePage/', homePage)


]
