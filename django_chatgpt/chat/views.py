from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import uuid

from .forms import MessageForm
from .models import Chat, Message
from .services import create_new_message, send_message_to_chatgpt


@login_required
def home(request):
    if request.method == "POST":
        pass
    else:
        chats = request.user.chats.all()
        form = MessageForm()
        return render(request, 'chat/index.html', {'form': form, 'chats': chats})


@login_required
def chat_list(request):
    if request.method == "POST":
        chat = Chat(title=str(uuid.uuid4()), owner=request.user)
        form = MessageForm(request.POST)
        if form.is_valid():
            chat.save()
            create_new_message(chat, form.save(commit=False))

            return redirect('chat:detail', chat_id=chat.id)

    else:
        # show default without chat
        form = MessageForm()
        chats = request.user.chats.all()

    return render(request, 'chat/index.html', {'form': form, 'chats': chats})


@login_required
def detail(request, chat_id):
    current_chat: Chat = get_object_or_404(Chat, pk=chat_id)
    chats = request.user.chats.all()

    if request.method == 'POST' and request.POST.get('action') == 'delete':
        current_chat.delete()
        return redirect('chat:list')
    else:
        form = MessageForm()

        return render(
            request, 'chat/index.html',
            {'form': form, 'current_chat': current_chat, 'chats': chats, 'message_list': current_chat.messages.all()})


@login_required
def message_index(request, chat_id):
    current_chat = get_object_or_404(Chat, pk=chat_id)

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            create_new_message(current_chat, form.save(commit=False))
            return redirect('chat:detail', chat_id=current_chat.id)

    else:
        # show default without chat
        form = MessageForm()

    return render(request, 'chat/index.html', {'form': form, 'chat': current_chat})
