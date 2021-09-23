from django.urls import path
from django.conf.urls import url

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    url('creategroup/', views.create_group),
    url('get-groups/', views.get_groups),
    url('get-group/(?P<pk>[0-9]+)/$', views.get_group),
]
