from django.urls import path, include
from .views import RegisterAchievementToUser, GetUserAchievements

urlpatterns = [
    path('register-achievement', RegisterAchievementToUser.as_view()),
    path('user-achievements', GetUserAchievements.as_view()),
]