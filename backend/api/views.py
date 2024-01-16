from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import serializers



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

class AchievementSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Achievement
        fields = ('id', 'name', 'code', 'description', 'points', 'category', 'latitude', 'longitude', 'start_date', 'end_date', 'start_time', 'end_time')

    def get_category(self, obj):
        return obj.get_category_display()

class UserAchievementSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer()
    class Meta:
        model = UserAchievement
        fields = ('achievement',)
class GetUserAchievements(APIView):
    def get(self, request):
        username = request.query_params.get("username")

        if not username:
            return Response({'error': 'No username specified'})
        
        user_achievements = UserAchievement.objects.filter(user__username=username)
        serializer = UserAchievementSerializer(user_achievements, many=True)

        return Response(serializer.data)

        #longitude = request.query_params.get("longitude")
        #latitude = request.query_params.get("latitude")
        #if longitude and latitude:
            