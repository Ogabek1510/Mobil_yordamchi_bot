from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import gapyuq_callback

mobiuz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🗒 Tarif rejalari", callback_data="mobiTarif")
        ],
        [
            InlineKeyboardButton(text='🛠 Xizmatlar', callback_data='mobiXizmat'),
        ],
        [
            InlineKeyboardButton(text="🌐 Internet paketlari", callback_data="mobiInternet")
        ],
        [
            InlineKeyboardButton(text="📞 Daqiqa paketlari", callback_data="mobiDaqiqa")
        ],
        [
            InlineKeyboardButton(text="✉️ SMS paketlari", callback_data="mobiSMS")
        ],
        [
            InlineKeyboardButton(text="#️⃣ USSD kodlari", callback_data="mobiUSSD")
        ],
    ])

# Tariflar uchun tugmalar:

tarif_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mobi turkumidagi tariflar", callback_data="Mobi")
        ],
        [
            InlineKeyboardButton(text="Internet uchun", callback_data="fornet")
        ],
        [
            InlineKeyboardButton(text='Yillik tariflar', callback_data="annual")
        ],
        [
            InlineKeyboardButton(text='Imtiyozli tariflar', callback_data="privil")
        ],
        [
            InlineKeyboardButton(text='Boshqa tariflar', callback_data="other")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_mobiuz")
        ],
    ])

mobi = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mobi 20", callback_data="mobi20"),
            InlineKeyboardButton(text="Mobi 25", callback_data="mobi25")
        ],
        [
            InlineKeyboardButton(text="Mobi 30+", callback_data="mobi30"),
            InlineKeyboardButton(text="Mobi 40", callback_data="mobi40")
        ],
        [
            InlineKeyboardButton(text="Mobi 50", callback_data="mobi50"),
            InlineKeyboardButton(text="Mobi 70", callback_data="mobi70")
        ],
        [
            InlineKeyboardButton(text="Mobi 90", callback_data="mobi90"),
            InlineKeyboardButton(text="Mobi 110", callback_data="mobi110")
        ],
        [
            InlineKeyboardButton(text="Mobi 150", callback_data="mobi150")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_tarif"),
            InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="back_mobiuz")
        ],
    ])

"""for_net = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gap yo'q", callback_data='gapyoq')
        ],
        [
            InlineKeyboardButton(text="Gap yo'q PRO", callback_data='gapyoqpro')
        ],
    ])"""


gap_yuq = {
    "Gap yo'q": "gapyoq",
    "Gap yo'q PRO": "gapyoqpro",
}

for_net = InlineKeyboardMarkup(row_width=1)
for key, value in gap_yuq.items():
    for_net.insert(InlineKeyboardButton(text=key, callback_data=gapyuq_callback.new(item_name=value)))
#   for_net.insert(tarif_menu)

annual = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Terminal yillik', callback_data='terminal'),
        ],
        [
            InlineKeyboardButton(text='Mobi 50 yillik', callback_data='mobi50_yil'),
            InlineKeyboardButton(text='Mobi 70 yillik', callback_data='mobi70_yil')
        ],
        [
            InlineKeyboardButton(text='Mobi 90 yillik', callback_data='mobi90_yil'),
            InlineKeyboardButton(text='Mobi 110 yilli', callback_data='mobi110_yil')
        ],
        [
            InlineKeyboardButton(text='Mobi 150 yillik', callback_data='mobi150_yil'),
        ],
    ]
)

services = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='afasffaf', callback_data='sada')
        ],
    ]
)


# Interenet paketlar uchun tugmalar:

net_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Oylik Internet paketlar', callback_data="MBoy"),
        ],
        [
            InlineKeyboardButton(text="Kunlik Internet paketlar", callback_data="MBkun")
        ],
        [
            InlineKeyboardButton(text="Tungi Internet paketlar", callback_data="MBtun")
        ],
        [
            InlineKeyboardButton(text="TAS-IX uchun Internet paketlar", callback_data="MBtasix")
        ],
        [
            InlineKeyboardButton(text="\"Ta'lim\" tarif rejasi uchun Internet paketlar", callback_data="MBtalim")
        ],
        [
            InlineKeyboardButton(text="\"Constructor\" tarif rejasi uchun Internet paketlar", callback_data="MBconstructor")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_mobiuz")
        ],
    ])

# Daqiqa paketlari uchun tugmalar:

daqiqa_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="100 Daqiqa", callback_data="100daq"),
            InlineKeyboardButton(text="300 Daqiqa", callback_data="300daq"),
        ],
        [
            InlineKeyboardButton(text="600 Daqiqa", callback_data="600daq"),
            InlineKeyboardButton(text="1200 Daqiqa", callback_data="1200daq"),
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_mobiuz"),
        ]
    ])

# SMS paketlari uchun tugmalar:

sms_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kunlik SMS paketlar", callback_data="SMSkun")
        ],
        [
            InlineKeyboardButton(text="Oylik SMS paketlar", callback_data="SMSoy")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_mobiuz")
        ],
    ])

# USSD kodlari uchun tugmalar

ussd_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_mobiuz")
        ]
    ]
)