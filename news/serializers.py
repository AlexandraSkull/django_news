from email.policy import default
from rest_framework import serializers

from .models import News

class NewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    watch_users = serializers.HiddenField(default=0)

    class Meta:
        model = News
        fields = ('title', 'content' , 'photo', 'created_at', 'updated_at',
            'is_published', 'user','category','watch_users'
        )