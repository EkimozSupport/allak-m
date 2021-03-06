from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from callsmusic import callsmusic, queues

import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT, UPDATES_CHANNEL, AUD_IMG, QUE_IMG, OWNER_NAME
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("oynat") & other_filters)
@errors
async def oynat(_, message: Message):

    lel = await message.reply("β’ **Δ°Επ»π΄πΌπ΄ π°π»πΈπ½π³πΈ** ππ΄π...")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="π£ πΊπ°π½π°π»",
                        url=f"https://t.me/SohbetDestek"),
                    InlineKeyboardButton(
                        text="β DΓΌznleyen",
                        url=f"https://t.me/Mahoaga")
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"β α΄ Ιͺα΄α΄α΄s Κα΄Ι΄Ι’α΄Κ α΄Κα΄Ι΄ {DURATION_LIMIT} α΄ΙͺΙ΄α΄α΄α΄(s) α΄Κα΄Ι΄'α΄ α΄ΚΚα΄α΄‘α΄α΄ α΄α΄ α΄Κα΄Κ!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("β¨ π±π°π½π° ππ΄π π³πΎπππ°ππΈπ½πΈ ππ΄ππ° πoutuBe π±π°Δπ»π°π½ππΈππΈπ½πΈ ππ΄ππΌπ΄π³Δ°π½Δ°π!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{QUE_IMG}",
        reply_markup=keyboard,
        caption=f"#β Δ°πππ΄π½π΄π½ Επ°ππΊπΈ **SΔ±raya** πΊπΎπ½ππΌπ³π° π΄πΊπ»π΄π½π³Δ° {position}!\n\nβ ππΎππππ±π΄ ππ°ππ°π΅πΈπ½π³π°π½ π³π΄πππ΄πΊπ»π΄π½πΌπ΄πΊππ΄π³Δ°π {bn}")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{AUD_IMG}",
        reply_markup=keyboard,
        caption=f"π§ **ΕΔ°πΌπ³Δ° πΎππ½πππΎπ** Δ°πππ΄π½Δ°π»π΄π½ π±Δ°π Επ°ππΊπΈ {costumer} !\n\nβ ππ°π»Δ°π° πΌΓπΔ°πΊ ππ°ππ°π΅πΈπ½π³π°π½ π³π΄πππ΄πΊπ»π΄π½πΌπ΄πΊππ΄π³Δ°π {bn}"
        )   
        return await lel.delete()
