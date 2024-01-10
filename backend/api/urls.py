from django.urls import path, include
from .views import RegisterAchievementToUser

urlpatterns = [
    path('register-achievement', RegisterAchievementToUser.as_view()),
]