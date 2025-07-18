from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

routers = DefaultRouter()
routers.register(r'conversations', ConversationViewSet, basename='conversation')

nested_router = NestedDefaultRouter(routers, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(routers.urls)),
    path('', include(nested_router.urls)),
]
