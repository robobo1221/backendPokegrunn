from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


from achievements.models import Achievement
from user.models import User, UserAchievement

class RegisterAchievementToUser(APIView):
    def post(self, request):
        achievement_code = request.data.get('achievement_code')
        username = request.data.get('username')

        try:
            achievement = Achievement.objects.get(code=achievement_code)
            user = User.objects.get(username=username)
        except (Achievement.DoesNotExist, User.DoesNotExist):
            return Response({'error': 'Invalid achievement code or username'}, status=status.HTTP_400_BAD_REQUEST)

        if UserAchievement.objects.filter(user=user, achievement=achievement).exists():
            return Response({'error': 'User already has this achievement'}, status=status.HTTP_400_BAD_REQUEST)
        
        current_datetime = datetime.now()

        # Check if current date and time are within achievement bounds (null-safe)
        if (
            (achievement.start_date and current_datetime.date() < achievement.start_date) if achievement.start_date else False or
            (achievement.end_date and current_datetime.date() > achievement.end_date) if achievement.end_date else False or
            (achievement.start_time and current_datetime.time() < achievement.start_time) if achievement.start_time else False or
            (achievement.end_time and current_datetime.time() > achievement.end_time) if achievement.end_time else False
        ):
            return Response({'error': 'Current date or time is outside achievement bounds'}, status=status.HTTP_400_BAD_REQUEST)

        user_achievement = UserAchievement(user=user, achievement=achievement)
        user_achievement.save()

        return Response({'success': 'Achievement registered successfully'}, status=status.HTTP_201_CREATED)