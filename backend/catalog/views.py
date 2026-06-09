from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . import services 

@api_view(['GET'])
def browse(request):
    if request.user.is_authenticated:
        data = services.browse(token)

        return Response({"recommendations": data})
