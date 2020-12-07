from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'title')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True,
                                        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    def validate_following(self, value):
        user = self.context['request'].user
        follow = Follow.objects.filter(user=user, following=value).exists()
        if user==value:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        return value

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following'])
            ]
