from user.models import User
from user.serializers import UserSerializer, UserSerializerWithoutID
from rest_framework import viewsets, status
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def return_http_200(self, response):
        '''Returns response with status code as 200.'''
        response.status_code = status.HTTP_200_OK
        return response

    def get_serializer_class(self):
        '''Overriding class to return User without an id.'''
        if self.action in ["retrieve"]:
            return UserSerializerWithoutID
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        '''Creating a new User.'''
        response = super().create(request, *args, **kwargs)
        return self.return_http_200(response)

    def update(self, request, *args, **kwargs):
        '''Updating exing User.'''
        response = super().update(request, *args, **kwargs)
        return self.return_http_200(response)

    def destroy(self, request, *args, **kwargs):
        '''Deleting a User'''
        response = super().destroy(request, *args, **kwargs)
        return self.return_http_200(response)
