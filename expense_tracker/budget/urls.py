from django.urls import path
from . import views
# from django.contrib.auth.views import CustomLoginView

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    # path('login/', CustomLoginView.as_view(), name='login'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
]
