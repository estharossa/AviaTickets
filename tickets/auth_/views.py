from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer
from rest_framework_jwt.views import obtain_jwt_token
from .models import Profile
import logging

logger = logging.getLogger(__name__)


class ProfilesView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser, FormParser]

    def create(self, request, *args, **kwargs):
        context = {
            'user': request.user
        }
        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.debug(f'Created profile with instance: {serializer.instance}')
        logger.info(f'Created profile with instance: {serializer.instance}')
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response("Not Authorized", status=status.HTTP_401_UNAUTHORIZED)
        profile = self.get_queryset().get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    logger.debug(f'Created user with instance: {serializer.instance}')
    logger.info(f'Created user with instance: {serializer.instance}')
    return Response({
        "user": UserSerializer(user, context=RegisterSerializer.context).data,
        "message": "User Created Successfully.  Now perform Login to get your token",
    })


# wrapper for the obtain_jwt_token
login = obtain_jwt_token
