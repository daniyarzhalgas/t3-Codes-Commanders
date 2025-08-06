from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import Order
from .serializers import OrderSerializer, OrderUpdateSerializer
from users.models import User


class OrderListCreateView(APIView):
    """
    Представление для создания и получения списка заказов
    """
    
    def get(self, request):
        """
        Получить список всех заказов
        """
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при получении заказов: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        Создать новый заказ с проверкой существования пользователя
        """
        try:
            # Проверка существования пользователя
            user_id = request.data.get('user')
            if not user_id:
                return Response({
                    'status': 'error',
                    'message': 'ID пользователя обязателен'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            if not User.objects.filter(id=user_id).exists():
                return Response({
                    'status': 'error',
                    'message': 'Пользователь с указанным ID не существует'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Заказ успешно создан',
                    'data': serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'status': 'error',
                    'message': 'Ошибка валидации данных',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({
                'status': 'error',
                'message': 'Ошибка валидации данных',
                'errors': e.message_dict if hasattr(e, 'message_dict') else str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при создании заказа: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrderDetailView(APIView):
    """
    Представление для получения, обновления и удаления заказа
    """
    
    def get(self, request, order_id):
        """
        Получить информацию о заказе по ID
        """
        try:
            order = get_object_or_404(Order, id=order_id)
            serializer = OrderSerializer(order)
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Заказ не найден'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при получении заказа: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, order_id):
        """
        Обновить информацию о заказе
        """
        try:
            order = get_object_or_404(Order, id=order_id)
            
            # Проверка существования пользователя при обновлении
            user_id = request.data.get('user')
            if user_id and not User.objects.filter(id=user_id).exists():
                return Response({
                    'status': 'error',
                    'message': 'Пользователь с указанным ID не существует'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            serializer = OrderUpdateSerializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Заказ успешно обновлен',
                    'data': OrderSerializer(order).data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 'error',
                    'message': 'Ошибка валидации данных',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Заказ не найден'
            }, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({
                'status': 'error',
                'message': 'Ошибка валидации данных',
                'errors': e.message_dict if hasattr(e, 'message_dict') else str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при обновлении заказа: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, order_id):
        """
        Удалить заказ
        """
        try:
            order = get_object_or_404(Order, id=order_id)
            order.delete()
            return Response({
                'status': 'success',
                'message': 'Заказ успешно удален'
            }, status=status.HTTP_204_NO_CONTENT)
        except Order.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Заказ не найден'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при удалении заказа: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserOrdersView(APIView):
    """
    Представление для получения заказов конкретного пользователя
    """
    
    def get(self, request, user_id):
        """
        Получить все заказы пользователя
        """
        try:
            # Проверка существования пользователя
            if not User.objects.filter(id=user_id).exists():
                return Response({
                    'status': 'error',
                    'message': 'Пользователь не найден'
                }, status=status.HTTP_404_NOT_FOUND)
            
            orders = Order.objects.filter(user_id=user_id)
            serializer = OrderSerializer(orders, many=True)
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при получении заказов пользователя: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 