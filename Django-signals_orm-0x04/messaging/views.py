from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from messaging.models import Message

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('home')

@cache_page(60)
@login_required
def conversation_view(request):
    messages = Message.objects.filter(receiver=request.user).select_related('sender').prefetch_related('replies')
    return render(request, 'chats/conversation.html', {'messages': messages})