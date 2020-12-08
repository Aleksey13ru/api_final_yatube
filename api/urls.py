from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts-list')
router.register('posts/(?P<post_id>.+)/comments', CommentViewSet,
                basename='comments-list')
router.register('follow', FollowViewSet, basename='follows-list')
router.register('group', GroupViewSet, basename='groups-list')

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(router.urls)),
    ]
