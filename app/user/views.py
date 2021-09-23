from django.http import JsonResponse
from rest_framework import generics, authentication, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.settings import api_settings
# from rest_framework.generics import CreateAPIView
from user.serializers import UserSerializer, AuthTokenSerializer, GroupSerializer
from core.models import Group

@api_view(['POST'])
def create_group(request):
    if request.method == 'POST':
        group_data = JSONParser().parse(request)
        group_serializer = GroupSerializer(data=group_data)
        if group_serializer.is_valid():
            group_serializer.save()
            return JsonResponse(group_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(group_serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_groups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
        group_serializer = GroupSerializer(groups, many=True)
        return JsonResponse(group_serializer.data, safe=False)

@api_view(['GET'])
def get_group(request, pk):
    if request.method == 'GET':
        group = Group.objects.get(id=pk)
        group_serializer = GroupSerializer(group, many=False)
        return JsonResponse(group_serializer.data)

class GroupListView():
    serializer_class = GroupSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
