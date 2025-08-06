from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import User
from .serializers import UserSerializer, UserUpdateSerializer


class UserListCreateView(APIView):
    """
    Представление для создания и получения списка пользователей
    """
    
    def get(self, request):
        """
        Получить список всех пользователей
        """
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при получении пользователей: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        Создать нового пользователя
        """
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Пользователь успешно создан',
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
                'message': f'Ошибка при создании пользователя: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDetailView(APIView):
    """
    Представление для получения, обновления и удаления пользователя
    """
    
    def get(self, request, user_id):
        """
        Получить информацию о пользователе по ID
        """
        try:
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(user)
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Пользователь не найден'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при получении пользователя: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, user_id):
        """
        Обновить информацию о пользователе
        """
        try:
            user = get_object_or_404(User, id=user_id)
            serializer = UserUpdateSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 'success',
                    'message': 'Пользователь успешно обновлен',
                    'data': UserSerializer(user).data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'status': 'error',
                    'message': 'Ошибка валидации данных',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Пользователь не найден'
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
                'message': f'Ошибка при обновлении пользователя: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, user_id):
        """
        Удалить пользователя
        """
        try:
            user = get_object_or_404(User, id=user_id)
            user.delete()
            return Response({
                'status': 'success',
                'message': 'Пользователь успешно удален'
            }, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({
                'status': 'error',
                'message': 'Пользователь не найден'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': f'Ошибка при удалении пользователя: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 