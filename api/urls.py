from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ModelViewSet, TicketViewSet, CommentViewSet


urlpatterns = [
    path('v1.0/auth/', include('djoser.urls')),
    path('v1.0/auth/', include('djoser.urls.authtoken')),
]

router = DefaultRouter()
router.register(r'v1.0/models', ModelViewSet, basename='user')
router.register(r'v1.0/tickets', TicketViewSet, basename='user')
router.register(r'v1.0/comments', CommentViewSet, basename='user')

urlpatterns += router.urls