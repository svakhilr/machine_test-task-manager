from rest_framework.views import APIView
from .models import CustomUser
from .token import get_tokens_for_user
from rest_framework import status,serializers
from rest_framework.response import Response

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    name = serializers.CharField()
    password = serializers.CharField()

class UserApiView(APIView):

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            if CustomUser.objects.filter(username= data["username"]).exists():
                return Response({"message":"Username already exists"},status=status.HTTP_400_BAD_REQUEST)
            data["role"] = CustomUser.USER
            user = CustomUser.objects.create_user(**data)
            tokens = get_tokens_for_user(user)
            return  Response({"tokens":tokens},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



