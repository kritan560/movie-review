from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.CreateUserFormView.as_view(), name='user-creation'),

]