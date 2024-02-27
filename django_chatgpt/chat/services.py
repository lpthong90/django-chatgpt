import os

from openai import OpenAI

from .models import Message


def create_new_message(chat, message):
    message.chat = chat
    message.role = Message.USER
    message.save()

    messages = chat.messages.last_many(5)

    bot_resonse_content = send_message_to_chatgpt(messages)
    chat.messages.create(
        content=bot_resonse_content,
        role=Message.SYSTEM
    )


def send_message_to_chatgpt(messages: list[Message]):
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=list(map(lambda m: m.openai_message, messages))
    )
    return completion.choices[0].message.content
