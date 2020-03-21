from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *


# Create your views here.
class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
