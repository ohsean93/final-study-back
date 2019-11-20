from django.shortcuts import render, get_object_or_404
from .serializers import TodoSerializers, UserSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializers(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status=400)


@api_view(['GET'])
def user_detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    if request.user != user:
        return Response(status=404)

    serializer = UserSerializers(user)
    return Response(serializer.data)


# @api_view(['get'])
# def todo_create(request):
#     serializer = TodoSerializers(data=request.POST)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(status=400)
