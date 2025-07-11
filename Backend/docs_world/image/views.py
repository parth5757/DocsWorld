from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestAPIView(APIView):
    def get(self, request):
        return Response({"message": "Jay Shree Krishna"}, status=status.HTTP_200_OK)