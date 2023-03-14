from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client("session", api_id='28679536', api_hash='21122f262849eea68e225f0dabc94532')


chat_id = "@datinganon_bot"

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Вам найден собеседник, начинайте диалог." in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(2.1)
        await app.send_message(chat_id, "Приветик я  Д19,я тут только ради интима!")
        sleep(2.2)
        await app.send_message(chat_id, "Я кончила 13раз за один подход посмотришь?)💦")

        if "Вам найден собеседник, начинайте диалог." in message.text:
                sleep(2.3)
                await app.send_sticker(chat_id, "CAACAgIAAxkBAAEIEzdkCxZqeIgOw1RO0TDMwjcJ6s87bQAC5yQAAgTbuErwHbfUyBhwFi8E")
                sleep(2.4)

                if "Вам найден собеседник, начинайте диалог." in message.text:  # Меняем это значение если хотим спамить в другом чате
                       await app.send_message(chat_id, "/stop")
                       sleep(2.5)
                       await app.send_message(chat_id, "/next")


app.run()
