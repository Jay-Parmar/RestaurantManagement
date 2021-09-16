from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer, UserDetailSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class IsAuthenticatedOrCreate(IsAuthenticated):
    '''Overriding has_permission '''
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super().has_permission(request, view)

def check_current_user(request, *args, **kwargs):
    '''Checks if the user is same as authorised user.'''
    print(kwargs)
    user_id = kwargs['pk']
    try:
        user = User.objects.get(id=user_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    print("CHECK: ", request.user, user, request.user==user)
    return request.user==user


class UserLoginView(APIView):
    '''
    View for user when logging in.
    '''
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        print("username ::: ", request.user)
        try:
            user = User.objects.get(email=request.data["email"])
            password = request.data["password"]
            print("User ::: ", user, password)
            if user.check_password(password):
                user_data = UserSerializer(user).data
                token = Token.objects.create(user=user).key
                return Response({**user_data, 'token': token}, status=status.HTTP_200_OK)
            else:
                return Response({"password": "Does not match"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
                return Response({"user": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):
    """
    View for user when logging out.
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        try:
            request.user.auth_token.delete()
        except Exception:
            pass
        return Response({"success": ("Successfully logged out.")}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrCreate,)
    authentication_classes = (TokenAuthentication,)

    def return_http_200(self, response):
        '''Returns response with status code as 200.'''
        response.status_code = status.HTTP_200_OK
        return response

    def get_serializer_class(self):
        '''Overriding class to return User without an id.'''
        if self.action in ["retrieve"]:
            return UserDetailSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        '''Create a new User.'''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({**serializer.data, "token": token.key}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        should_allow = check_current_user(request, *args, **kwargs)
        if not should_allow:
            return Response({"error": "Request Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        '''Updating exing User.'''
        should_allow = check_current_user(request, *args, **kwargs)
        if not should_allow:
            return Response({"error": "Request Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
        response = super().update(request, *args, **kwargs)
        return self.return_http_200(response)

    def destroy(self, request, *args, **kwargs):
        '''Deleting a User'''
        should_allow = check_current_user(request, *args, **kwargs)
        if not should_allow:
            return Response({"error": "Request Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
        response = super().destroy(request, *args, **kwargs)
        return self.return_http_200(response)
