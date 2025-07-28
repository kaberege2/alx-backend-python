from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from messaging.models import Message
from messaging.serializers import MessageSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user, sender=self.request.user).select_related('sender').prefetch_related('replies').only('id', 'sender', 'receiver', 'content', 'timestamp')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

@method_decorator(cache_page(60), name='dispatch')
class CachedConversationView(MessageListCreateView):
    pass

class UnreadMessagesView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.unread.unread_for_user(self.request.user)
