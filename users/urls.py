from django.urls import path
from users import views
from .views import *

# urlpatterns = [
#     path('register/', views.register),
#     path('confirm/', views.confirm),
#     path('login/', views.login_view),
# ]


urlpatterns = [
    path('users/register/', views.RegisterAPIview),
    path('users/confirm/', views.ConfirmAPIview),
    path('users/login/', views.LoginAPIview),
]