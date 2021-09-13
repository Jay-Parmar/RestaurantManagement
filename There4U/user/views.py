from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def user_view(request):

    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            pk = request.GET['pk']
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            return JsonResponse(str(err), status=status.HTTP_404_NOT_FOUND, safe=False)
        
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == "GET":
        try:
            pk = request.GET['pk']
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            return JsonResponse(str(err), status=status.HTTP_404_NOT_FOUND, safe=False)
        
        data = UserSerializer(user).data
        return JsonResponse(data, status=status.HTTP_200_OK)


    elif request.method == 'DELETE':
        try:
            pk = request.GET['pk']
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            return JsonResponse(str(err), status=status.HTTP_404_NOT_FOUND, safe=False)
        
        user.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)








