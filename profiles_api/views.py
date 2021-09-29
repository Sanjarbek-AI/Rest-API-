from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles_api.serializers import HelloSerializer


class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Get all the objects from database"""

        an_api_view = [
            'Book', 'Week', 'Small', 'Good'
        ]

        return Response({'message': 'Hello World !', 'api': an_api_view})

    def post(self, request):
        """Create Hello World API"""

        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """helps to update object"""

        return Response({"message": 'PUT'})

    def patch(self, request, pk=None):
        """helps to update object"""

        return Response({"message": 'PATCH'})

    def delete(self, request, pk=None):
        """helps to delete object"""

        return Response({"message": 'DELETE'})


class HelloViewset(viewsets.ViewSet):
    """Test API with viewset."""

    def list(self, request):
        a_viewset = [
            'Book', 'Week', 'Small', 'Good'
        ]
        return Response({"message": a_viewset, "name": "Viewset"})
