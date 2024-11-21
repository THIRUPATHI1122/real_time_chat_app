from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('members/', views.members_list, name='members_list'),
    path('chat/<int:user_id>/', views.chat_view, name='chat'),
]
