from django.urls import path
from .views import *

urlpatterns = [

    # Project paths
    path('create', create.as_view()),
    path('get_user', getUser.as_view()),


]