from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import CabinetUserSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cabinet_orders(request):
    serializer = CabinetUserSerializer(request.user)
    return Response(serializer.data)
