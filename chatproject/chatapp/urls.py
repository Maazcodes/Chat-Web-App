from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from chatapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('user/<int:user_id>/update/', views.UserUpdateView.as_view(), name="user_update"),
    path("signup/", views.signup, name="signup"),
    path("login/", LoginView.as_view(template_name = "login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name = "logout.html"), name="logout"),
    path("users/", views.UserListView.as_view(), name="users")
]