from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_beeline import beeline_callback, tarif_callback

# Beeline menu

menu_buttons = {
    "🗒 Tarif rejalari": "beelineTarif",
    "🛠 Xizmatlar": "beelineXizmat",
    "🌐 Internet paketlari": "beelineInternet",
    "📞 Daqiqa paketlari": "beelineDaqiqa",
    "✉️ SMS paketlari": "beelineSMS",
    "#️⃣ USSD kodlari": "beelineUSSD",
}

beeline = InlineKeyboardMarkup(row_width=1)
for key, value in menu_buttons.items():
    beeline.insert(InlineKeyboardButton(text=key, callback_data=beeline_callback.new(item_name=value)))


# Tariflar uchun tugmalar:

tarif_buttons = {
    "Zo'r 3": "zor3",
    "Zo'r 5": "zor5",
    "Zo'r 7": "zor7",
    "Zo'r 12": "zor12",
    "Zo'r 20": "zor20",
    "Status Silver": "status_silver",
    "Status Gold": "status_gold",
    "Status Platinum": "status_platinum",
    "Oson 1": "oson1",
    "Oson 10": "oson10",
    "Allo": "allo",
    "Kunlik": "kunlik",
    "Click+": "click+",
}

tarif = InlineKeyboardMarkup(row_width=2)
for key, value in tarif_buttons.items():
    tarif.insert(InlineKeyboardButton(text=key, callback_data=tarif_callback.new(item_name=value)))
tarif.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_beeline"))
tarif.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))

# Interenet paketlar uchun tugmalar:

netpaket = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="Ortga", callback_data="back_beeline")
        ],
    ])

# Daqiqa paketlari uchun tugmalar:

daqiqa = InlineKeyboardMarkup(
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
            InlineKeyboardButton(text="Ortga", callback_data="back_beeline"),
        ]
    ])

# SMS paketlari uchun tugmalar:

sms = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kunlik SMS paketlar", callback_data="SMSkun")
        ],
        [
            InlineKeyboardButton(text="Oylik SMS paketlar", callback_data="SMSoy")
        ],
        [
            InlineKeyboardButton(text="Ortga", callback_data="back_beeline")
        ],
    ])

# USSD kodlari uchun tugmalar

ussd = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ortga", callback_data="back_beeline")
        ]
    ]
)