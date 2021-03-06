from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>β¨ **π·πΎΕπΆπ΄π»π³Δ°π½Δ°π {message.from_user.first_name}** \n
π­ **[Elly&carl Music](https://t.me/Ellycarlmusicbot) ππ΄π½Δ° ππ΄π»π΄πΆππ°πΌ'πΈπ½ ππ΄ππ»Δ° ππΎπ·π±π΄ππ»π΄πΔ°ππ»π΄ πΆπππΏπ»π°ππΈπ½π³π° πΌΓπΔ°πΊ Γπ°π»πΌπ°ππΈπ½π° Δ°πΔ°π½ ππ΄πΔ°π½!**

π‘ **Γππ΄πΔ°π½π΄ ππΈπΊπ»π°ππ°ππ°πΊ π±πΎπ'ππ½ πΓπΌ πΊπΎπΌπππ»π°ππΈπ½πΈ ππ΄ π½π°ππΈπ» Γπ°π»πΈΕππΈΔπΈπ½πΈ ΓΔππ΄π½Δ°π½. Β» π πΊπΎπΌπππ»π°π π³ΓΔπΌπ΄πΔ°!**

β **π±π π±πΎπ'ππ½ πΓπΌ Γππ΄π»π»Δ°πΊπ»π΄πΔ° π·π°πΊπΊπΈπ½π³π° π³π°π·π° π΅π°ππ»π° π±Δ°π»πΆΔ° Δ°ΓΔ°π½, ππ°π³π΄π²π΄ π±π°ππΈπ½πΈπ /help**

β **Gruplar'π³a πΌΓπΔ°πΊ Γπ°π»πΌπ°πΊ Δ°ΓΔ°π½ [AdsΔ±z Kaptan](hptts://t.me/Kizilsancaksahibi) ππ°ππ°π΅πΈπ½π³π°π½ ππ°πΏπΈπ»πΌπΈΕππΈπ.**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "β π±π΄π½Δ° πΆπππ±ππ½π° π΄πΊπ»π΄ β", url=f"https://t.me/Ellycarlmusicbot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "π πΊπΎπΌπππ»π°π", url="https://t.me/UcretliBotlar"
                    ),
                    InlineKeyboardButton(
                        "π₯οΈ π³Γππ΄π½π»π΄πΌπ΄ ππ°πΏπ°π½", url=f"https://t.me/Kizilsancaksahibi")
                ],[
                    InlineKeyboardButton(
                        "π₯ ππ΄ππΌΔ° πΆπππΏ", url=f"https://t.me/Smailesi"
                    ),
                    InlineKeyboardButton(
                        "π£ ππ΄ππΌΔ° πΊπ°π½π°π»", url=f"https://t.me/Kizilsancakbilgi")               
                 ],[
                    InlineKeyboardButton(
                        "π§ͺ πΊπ°ππ½π°πΊ πΊπΎπ³π π§ͺ", url="https://t.me/kizilsancaksahibi"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@Ellycarlmusicbot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""β **Κα΄α΄ Ιͺs Κα΄Ι΄Ι΄ΙͺΙ΄Ι’**\n<b>β£ **α΄α΄α΄Ιͺα΄α΄:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β’ πΆπππΏ", url=f"https://t.me/ucretliBotlar"
                    ),
                    InlineKeyboardButton(
                        "π£ πΊπ°π½π°π»", url=f"https://t.me/Smailesi"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@ellycarlmusicbor"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>β’ Κα΄ΚΚα΄ {message.from_user.mention()}, α΄Κα΄α΄sα΄ α΄α΄α΄ α΄Κα΄ Κα΄α΄α΄α΄Ι΄ Κα΄Κα΄α΄‘ α΄α΄ sα΄α΄ α΄Κα΄ Κα΄Κα΄ α΄α΄ssα΄Ι’α΄ Κα΄α΄ α΄α΄Ι΄ Κα΄α΄α΄ ?α΄Κ α΄sΙͺΙ΄Ι’ α΄ΚΙͺs Κα΄α΄</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="β π±π΄π½Δ° π½π°ππΈπ» πΊππ»π»π°π½πΈπππΈπ½", url=f"https://t.me/Ellycarlmusicbot?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba {message.from_user.mention()}, yardΔ±m menΓΌsΓΌne hoΕ geldinizβ¨
\nπ π±π΄π½Δ° π½π°ππΈπ» πΊππ»π»π°π½πΈπππΈπ½?
\n1. ΓΆnce beni grubunuza ekleyin.
2. beni yΓΆnetici olarak tanΔ±tΔ±n ve tΓΌm izinleri verin.
3. ardΔ±ndan, @taliaMusicasistant grubunuza veya tΓΌrΓΌnΓΌze /userbotjoin.
3. mΓΌzik Γ§almaya baΕlamadan ΓΆnce sesli sohbeti aΓ§tΔ±ΔΔ±nΔ±zdan emin olun.
\nππ»ββοΈ **tΓΌm kullanΔ±cΔ± iΓ§in komutlar:**
\n/play (song name) - youtube'dan ΕarkΔ± Γ§almak
/oynat (reply to audio) - ses dosyasΔ±nΔ± kullanarak ΕarkΔ± Γ§alma youtube linki veya Mp3 oynatΔ±cΔ±
/playlist - listedeki ΕarkΔ±yΔ± sΔ±rada gΓΆsterme
/song (song name) - youtube'dan ΕarkΔ± indirme
/search (video name) - youtube'dan video arama detayΔ±
/vsong (video name) - youtube'dan video indirme ayrΔ±ntΔ±lΔ±
/lyric - (song name) ΕarkΔ± sΓΆzleri scrapper 
/vk (song name) - ΕarkΔ±yΔ± satΔ±r iΓ§i moddan indirme
\nπ·π»ββοΈ **yΓΆneticiler iΓ§in komutlar:**
\n/player - mΓΌzik Γ§alar ayarlarΔ± panelini aΓ§ma
/pause - mΓΌzik akΔ±ΕΔ±nΔ± duraklatma
/resume - devam et mΓΌzik duraklatΔ±ldΔ± 
/skip - sonraki ΕarkΔ±ya atlamak 
/end - mΓΌzik akΔ±ΕΔ±nΔ± durdurma 
/userbotjoin - grubunuza asistan katΔ±lmayΔ± davet etme 
/reload - yΓΆnetici listesini yenilemek iΓ§in 
/cache - temizlenmiΕ yΓΆnetici ΓΆnbelleΔi iΓ§in 
/auth - mΓΌzik botu kullanmak iΓ§in yetkili kullanΔ±cΔ± 
/deauth - mΓΌzik botu kullanmak iΓ§in yetkisiz 
/musicplayer (on / off) - devre dΔ±ΕΔ± bΔ±rakmak / etkinleΕtirmek grubunuzdaki mΓΌzik Γ§alar iΓ§in
\nπ§ kanal akΔ±ΕΔ± komutlarΔ±:
\n/cplay - kanal sesli sohbetinde mΓΌzik akΔ±ΕΔ± 
/cplayer - ΕarkΔ±yΔ± akΔ±Εta gΓΆsterme 
/cpause - mΓΌzik akΔ±ΕΔ±nΔ± duraklatma 
/cresume - akΔ±ΕΔ±n duraklatΔ±ldΔ±ΔΔ±nΔ± sΓΌrdΓΌrme 
/cskip - akΔ±ΕΔ± bir sonraki ΕarkΔ±ya atlamak 
/cend - mΓΌzik akΔ±ΕΔ±nΔ± sonlandΔ±rmak 
/admincache - yΓΆnetici ΓΆnbelleΔini yenileme 
\nπ§ββοΈ sudo kullanΔ±cΔ±larΔ± iΓ§in komut:
\n/userbotleaveall - asistanΔ±n tΓΌm gruptan ayrΔ±lmasΔ±nΔ± emretmek 
/gcast - yayΔ±n iletisi gΓΆnderme yardΔ±mcΔ±ya gΓΆre 
\nπ **eΔlence iΓ§in komutlar:**
\n/chika - kendiniz kontrol edin 
/wibu - kendiniz kontrol edin 
/asupan - kendiniz kontrol edin
/truth - kendiniz kontrol edin
/dare - kendiniz kontrol edin
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β£ πΆπππΏ", url=f"https://t.me/Smailesi"
                    ),
                    InlineKeyboardButton(
                        "π£ πΊπ°π½π°π»", url=f"https://t.me/Ucretlibotlar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "βπ»βπ» πΆπ΄π»Δ°ΕπΔ°πΔ°π²Δ°", url=f"https://t.me/kizilsancaksahibi"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@ellycarlmusicbot"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("α΄ΙͺΙ΄Ι’ΙͺΙ΄Ι’...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "β `α΄α΄Ι΄Ι’!!`\n"
        f"β£ `{delta_ping * 1000:.3f} α΄s`"
    )


@Client.on_message(command(["uptime", f"uptime@Efsanestar_bot"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "π€ Κα΄α΄ sα΄α΄α΄α΄s:\n"
        f"β€ **α΄α΄α΄Ιͺα΄α΄:** `{uptime}`\n"
        f"β€ **sα΄α΄Κα΄ α΄Ιͺα΄α΄:** `{START_TIME_ISO}`"
    )
