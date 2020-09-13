from rest_framework import serializers

from .models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
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
    user = serializers.ReadOnlyField(source='user.username')
    following = serializers.SlugRelatedField(
        many=False,
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

    def validate(self, data):
        current_user = self.context['request'].user
        data_user = data['following']

        if  current_user == data_user:
            raise serializers.ValidationError(
                f"Нельзя подписаться на самого себя")

        followings = Follow.objects.filter(
            user=current_user).filter(following=data_user)
        if followings.exists():
            raise serializers.ValidationError(
                f"Вы уже подписаны на автора {data_user}")

        return data
