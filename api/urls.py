from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = DefaultRouter()

router.register('v1/posts', PostViewSet, basename='posts-list')
router.register('v1/posts/(?P<post_id>.+)/comments', CommentViewSet,
                basename='comments-list')
router.register('v1/follow', FollowViewSet, basename='follows-list')
router.register('v1/group', GroupViewSet, basename='groups-list')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]

urlpatterns += router.urls
