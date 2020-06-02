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
    following = serializers.CharField(source='following.username')

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

    def validate(self, data):
        author = data['following']
        following_user = User.objects.filter(username=author['username'])
        if not following_user.exists():
            raise serializers.ValidationError(
                f"Автор не найден {author['username']}")

        follow_user = User.objects.get(username=author['username'])
        if self.context['request'].user == follow_user:
            raise serializers.ValidationError(
                f"Нельзя подписаться на самого себя")

        followings = Follow.objects.filter(
            user=self.context['request'].user).filter(following=follow_user)
        if followings.exists():
            raise serializers.ValidationError(
                f"Вы уже подписаны на автора {follow_user.username}")

        data['following'] = follow_user

        return data
