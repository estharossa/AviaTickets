from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from airflow.models import FlightOrder
from airflow.utils.constants import PROCESS_OK


@api_view(['GET'])
@permission_classes([IsAdminUser])
def process_order(request, order_id):
    order = FlightOrder.objects.get(id=order_id)
    if not order:
        return Response("No such order", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    order.status = PROCESS_OK
    order.save()
    return Response("Order has successfully paid", status=status.HTTP_200_OK)
