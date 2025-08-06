from django.urls import path
from .views import OrderListCreateView, OrderDetailView, UserOrdersView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('users/<int:user_id>/orders/', UserOrdersView.as_view(), name='user-orders'),
] 