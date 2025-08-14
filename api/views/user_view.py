from api.models.user import User
from api.serializers.user_serializer import UserSerializer
from django.db import IntegrityError
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {"message": "User created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except DRFValidationError as e:
            return Response(
                {"error": e.detail}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError:
            return Response(
                {"error": "A user with this name or email already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(
                {"message": "User updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except DRFValidationError as e:
            return Response(
                {"error": e.detail},
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError:
            return Response(
                {"error": "A user with this name or email already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(
                {"message": "User deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )