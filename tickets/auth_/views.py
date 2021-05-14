from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from rest_framework_jwt.views import obtain_jwt_token
import logging

logger = logging.getLogger(__name__)


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
