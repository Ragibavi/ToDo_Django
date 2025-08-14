from api.models.todo import ToDo
from api.serializers.todo_serializer import ToDoSerializer
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.response import Response

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                {"message": "ToDo created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except DRFValidationError as e:
            return Response(
                {"error": e.detail},
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
                {"message": "ToDo updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                {"error": "ToDo not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except DRFValidationError as e:
            return Response(
                {"error": e.detail},
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
                {"message": "ToDo deleted successfully"},
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                {"error": "ToDo not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
