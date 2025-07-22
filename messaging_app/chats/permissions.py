from rest_framework.permissions import BasePermission

class IsParticipantOfConversation(BasePermission):
    message = "You are not a participant of this conversation."

    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()
