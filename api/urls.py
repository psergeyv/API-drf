from rest_framework.routers import DefaultRouter
from .views import CommentsViewSet, GroupViewSet, FollowViewSet, PostList, PostDetail
from django.urls import path, include
from rest_framework.authtoken import views

router = DefaultRouter()
#router.register(r'posts', PostViewSet, basename="posts")
router.register(r'posts/(?P<post_id>\d+)/comments', CommentsViewSet, basename='comments')
router.register(r'group', GroupViewSet, basename="groups")
#router.register(r'follow', FollowViewSet, basename="follows")

urlpatterns = [    
    path(r'posts/', PostList.as_view()),
    path(r'posts/<int:pk>/', PostDetail.as_view()),
    path(r'follow/', FollowViewSet.as_view()),

    path('', include(router.urls)),    
]