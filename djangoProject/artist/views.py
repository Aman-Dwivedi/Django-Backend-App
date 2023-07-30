from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import logging
from django.contrib.auth.models import User
logger = logging.getLogger(__name__)

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        ret = User.objects.get(username=request.data["username"], password=request.data["password"])
        if ret:
            token, created = Token.objects.get_or_create(user=ret)
            return Response({
                'token': token.key,
                'user_id': ret.pk,
                'email': ret.username
            })
