from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import User
from api.serializers import UserSerializer

from api.permissions import IsLoggedInUserOrAdmin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsLoggedInUserOrAdmin]
        return [permission() for permission in permission_classes]

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)