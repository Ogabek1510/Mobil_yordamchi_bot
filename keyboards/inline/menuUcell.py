from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ucell = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🗒 Tarif rejalari', callback_data='ucellTarif'),
        ],
        [
            InlineKeyboardButton(text='🛠 Xizmatlar', callback_data='ucellXizmat'),
        ],
        [
            InlineKeyboardButton(text='🌐 Internet paketlari', callback_data='ucellInternet')
        ],
        [
            InlineKeyboardButton(text='📞 Daqiqa paketlari', callback_data='ucellDaqiqa')
        ],
        [
            InlineKeyboardButton(text='✉️ SMS paketlari', callback_data='ucellSMS')
        ],
        [
            InlineKeyboardButton(text='#️⃣ USSD kodlari', callback_data='ucellUSSD')
        ],
    ])

tarif_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Faol tarif rejalar', callback_data="Faol")
        ],
        [
            InlineKeyboardButton(text='⭕️ Imtiyozli tarif rejalar', callback_data="Imtiyoz")
        ],
        [
            InlineKeyboardButton(text='💰 Units tarif rejalari', callback_data="Units")
        ],
        [
            InlineKeyboardButton(text='◀️ Ortga', callback_data="back_ucell")
        ],
    ]
)

net_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌐 Oylik Internet paketlar', callback_data="MB_Oy"),
        ],
        [
            InlineKeyboardButton(text="🌐 Kunlik Internet paketlar", callback_data="MB_Kun")
        ],
        [
            InlineKeyboardButton(text="🌐 Tungi Internet paketlar", callback_data="MB_Tun")
        ],
        [
            InlineKeyboardButton(text="🌐 TAS-IX uchun Internet paketlar", callback_data="MB_TAS-IX")
        ],
        [
            InlineKeyboardButton(text="🌐 \"Ta'lim\" tarif rejasi uchun Internet paketlar", callback_data="MB_Talim")
        ],
        [
            InlineKeyboardButton(text="🌐 \"Constructor\" tarif rejasi uchun Internet paketlar", callback_data="MB_Const")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_ucell")
        ],
    ])

# Daqiqa paketlari uchun tugmalar:

daqiqa_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📞 100 Daqiqa", callback_data="100daq"),
            InlineKeyboardButton(text="📞 300 Daqiqa", callback_data="300daq"),
        ],
        [
            InlineKeyboardButton(text="📞 600 Daqiqa", callback_data="600daq"),
            InlineKeyboardButton(text="📞 1200 Daqiqa", callback_data="1200daq"),
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_ucell"),
        ]
    ])

# SMS paketlari uchun tugmalar:

sms_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✉️ Kunlik SMS paketlar", callback_data="SMS_Kun")
        ],
        [
            InlineKeyboardButton(text="✉️ Oylik SMS paketlar", callback_data="SMS_Oy")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_ucell")
        ],
    ])

ussd_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_ucell")
        ]
    ])