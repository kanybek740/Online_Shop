from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('edit/<int:pk>', views.edit_user, name='edit_user'),
]