from django.shortcuts import render, get_object_or_404, redirect
import uuid

from .forms import MessageForm
from .models import Chat, Message


def chat_list(request):
    if request.method == "POST":
        chat = Chat(title=str(uuid.uuid4()))
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat  # Associate the message with the retrieved chat
            message.save()  # Save the message to the database
            return redirect('chat_detail', chat_id=chat.id)

    else:
        # show default without chat
        form = MessageForm()
        chats = Chat.objects.all()

    return render(request, 'chat/index.html', {'form': form, 'chats': chats})


def detail(request, chat_id):
    current_chat: Chat = get_object_or_404(Chat, pk=chat_id)
    chats = Chat.objects.all()

    if request.method == "DELETE":
        # delete chat
        # current_chat
        return redirect('chat_list')
    else:
        form = MessageForm()

        return render(
            request, 'chat/index.html',
            {'form': form, 'current_chat': current_chat, 'chats': chats, 'message_list': current_chat.messages.all()})


def message_index(request, chat_id):
    current_chat = get_object_or_404(Chat, pk=chat_id)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = current_chat # Associate the message with the retrieved chat
            message.save()  # Save the message to the database
            return redirect('chat_detail', chat_id=current_chat.id)

    else:
        # show default without chat
        form = MessageForm()

    return render(request, 'chat/index.html', {'form': form, 'chat': current_chat})
