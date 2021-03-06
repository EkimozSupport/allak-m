# Copyright (C) 2021 TaliaMusicProject


from asyncio import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from cache.admins import admins
from helpers.channelmusic import get_chat_id
from helpers.decorators import authorized_users_only, errors
from helpers.filters import command, other_filters
from callsmusic import callsmusic
from callsmusic.queues import queues


@Client.on_message(filters.command("reload"))
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text("β π±πΎπ ** π³πΎπΆππ πΓπΊπ»π΄π½π³Δ° ! **\nβ **πΓπ½π΄πΔ°π²Δ° π»Δ°πππ΄πΔ°** π³πΎΔππ **GΓΌncellenmiΕ!**")


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("β π°πΊπΈΕππ° π·Δ°Γπ±Δ°π Επ΄π ππΎπΊ!")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("β πΌΓπΔ°πΊ π³πππ°πΊπ»π°ππΈπ»π³πΈ!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("β π·Δ°Γπ±Δ°π Επ΄π π³πππ³ππππ»πΌπ°π!")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("β πΌΓπΔ°πΊ π³π΄ππ°πΌ π΄ππΔ°!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("β π°πΊπΈΕππ° π·Δ°Γπ±Δ°π Επ΄π ππΎπΊ!")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("β ππ°ππΈπ½ ππΎπ½π° π΄ππ³Δ°!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("β π°πΊπΈΕππ° π·Δ°Γπ±Δ°π Επ΄π ππΎπΊ π!")
    else:
        queues.task_done(chat_id)

        if queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"β π°ππ»π°ππΈπ»πΌπΈΕ : **{skip[0]}**\nβ ΕΔ°πΌπ³Δ° πΎππ½πππΎπ : **{qeue[0][0]}**")


@Client.on_message(filters.command("auth"))
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("β πΊππ»π»π°π½πΈπ²πΈππΈ ππ΄ππΊΔ°π»π΄π½π³Δ°ππΌπ΄πΊ Δ°ΓΔ°π½ πΌπ΄ππ°πΉπ° π²π΄ππ°πΏ ππ΄πΔ°π½!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("user authorized.")
    else:
        await message.reply("β πΊππ»π»π°π½πΈπ²πΈ ππ°ππ΄π½ ππ΄ππΊΔ°π»Δ°!")


@Client.on_message(filters.command("deauth"))
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("β πΊππ»π»π°π½πΈπ²πΈππΈ ππ΄ππΊΔ°πΔ°ππ»π΄ΕπΔ°ππΌπ΄πΊ Δ°ΓΔ°π½ πΌπ΄ππ°πΉ π°ππΈπ½!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("user deauthorized")
    else:
        await message.reply("β KULLANICI ZATEN YETKΔ°LENDΔ°RΔ°LDΔ°!")
