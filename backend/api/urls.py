from django.urls import path, include
from .views import RegisterAchievementToUser, GetUserAchievements, GetAchievements

urlpatterns = [
    path('register-achievement', RegisterAchievementToUser.as_view()),
    path('user-achievements', GetUserAchievements.as_view()),
    path('achievements', GetAchievements.as_view()),
]