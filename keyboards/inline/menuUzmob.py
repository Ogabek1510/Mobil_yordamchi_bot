from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_uzmob import uzmob_callback, tarif_callback, service_callback, net_callback, activ_callback, privil_callback, units_callback, oy_callback,kun_callback

# Uzmobile menyu tugmalar

menu_buttons = {
    "🗒 Tarif rejalari": "UzmobiTarif",
    "🛠 Xizmatlar": "UzmobiXizmat",
    "🌐 Internet paketlari": "UzmobiInternet",
    "📞 Daqiqa paketlari": "UzmobiDaqiqa",
    "✉️ SMS paketlari": "UzmobiSMS",
    "#️⃣ USSD kodlari": "UzmobiUSSD",
}

uzmob = InlineKeyboardMarkup(row_width=1)
for key, value in menu_buttons.items():
    uzmob.insert(InlineKeyboardButton(text=key, callback_data=uzmob_callback.new(item_name=value)))

# Tariflar uchun tugmalar:

tarif_buttons = {
    "✅ Faol tarif rejalar": "Faol",
    "⭕️ Imtiyozli tarif rejalar": "Imtiyoz",
    "💰 Units tarif rejalari": "Units",
}

tarif_menu = InlineKeyboardMarkup(row_width=1)
for key, value in tarif_buttons.items():
    tarif_menu.insert(InlineKeyboardButton(text=key, callback_data=tarif_callback.new(item_name=value)))
tarif_menu.insert(InlineKeyboardButton(text='◀️ Ortga', callback_data="back_uzmob"))

# faol tarif rejalar:

activ_buttons = {
    "Oddiy 10": "Oddiy10",
    "Street": "Street",
    "Onlime": "Onlime",
    "Flash": "Flash",
    "Ishbilarmon": "Ishbil",
    "Street Upgrade": "StreetUp",
    "Royal": "Royal",
    "Flash Upgrade": "FlashUp",
}

activ = InlineKeyboardMarkup(row_width=2)
for key, value in activ_buttons.items():
    activ.insert(InlineKeyboardButton(text=key, callback_data=activ_callback.new(item_name=value)))
activ.insert(InlineKeyboardButton(text='◀️ Ortga', callback_data="back_uzmob_tarif"))
activ.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))

# Imtiyozli tarif rejalar:

privil_buttons = {
    "🎓 Ta'lim": "Talim",
    "🏫 Maktab": "Maktab",
    "👨‍🎓 Yoshlar": "Yoshlar",
    "🧒 Bolajon": "Bolajon",
}

privil = InlineKeyboardMarkup(row_width=2)
for key, value in privil_buttons.items():
    privil.insert(InlineKeyboardButton(text=key, callback_data=privil_callback.new(item_name=value)))
privil.insert(InlineKeyboardButton(text='◀️ Ortga', callback_data="back_uzmob_tarif"))
privil.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))

# Units turkum tarif rejalar

units_buttons = {
    "Units 700": "units700",
    "Units 1500": "units1500",
    "Units 4000": "units4000",
    "Units 8000": "units8000",
    "Units 11000": "units11000",
    "Units 14000": "units14000",
    "Units 18000": "units18000",
    "Units 22000": "units22000",
}

units = InlineKeyboardMarkup(row_width=2)
for key, value in units_buttons.items():
    units.insert(InlineKeyboardButton(text=key, callback_data=units_callback.new(item_name=value)))
units.insert(InlineKeyboardButton(text='◀️ Ortga', callback_data="back_uzmob_tarif"))
units.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))

# Xizmatlar uchun tugmalar

services_buttons = {
    "\"Qabul qilinmagan qo'ng'iroqlar\" va \"Tarmoqda\"": "tarmoqda",
    "LTE (4G)": "4G",
    "Limitsiz ovoz": "voice",
    "Megabaytlarni tezkor o'tkazish": "transferMB",
    "Restart": "restart",
    "Ovozli pochta": "voice_mail",
    "Tungi qo'ng'iroqlar": "night_call",
    "Oila uchun": "family",
    "Yashirin qo'ng'iroq": "hidden_call",
    "Shaxsiy raqam uzatilishini taqiqlash": "hidden_number",
    "Tezkor o'tkazmalar": "fast_transfer",
    "YHQ jarimalari haqida xabar": "fines",
    "Chaqiriqni kutish va ushlab turish": "load",
    "Yo'naltirish": "rederect",
    "Taqiqlash": "ban",
    "Abonent bo'limi xizmatlari": "service",

}

services = InlineKeyboardMarkup(row_width=2)
for key, value in services_buttons.items():
    services.insert(InlineKeyboardButton(text=key, callback_data=service_callback.new(item_name=value)))
services.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob"))

# Interenet paketlar uchun tugmalar:

net_buttons = {
    "🌐 Oylik Internet paketlar": "MB_Oy",
    "🌐 Kunlik Internet paketlar": "MB_Kun",
    "🌐 Tungi Internet paketlar": "MB_Tun",
    "🌐 TAS-IX uchun Internet paketlar": "MB_TAS-IX",
    "🌐 Internet NON-STOP": "non-stop",
    "🌐 \"Ta'lim\" tarif rejasi uchun Internet paketlar": "MB_Talim",
}

net_menu = InlineKeyboardMarkup(row_width=1)
for key, value in net_buttons.items():
    net_menu.insert(InlineKeyboardButton(text=key, callback_data=net_callback.new(item_name=value)))
net_menu.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob"))


oy_buttons = {
    "500 MB": "500mb_oy",
    "1500 MB": "1500mb",
    "3000 MB": "3000mb",
    "5000 MB": "5000mb",
    "8000 MB": "8000mb",
    "12000 MB": "12000mb",
    "20000 MB": "20000mb",
    "30000 MB": "30000mb",
    "50000 MB": "50000mb",
    "75000 MB": "75000mb",
}
oy_MB = InlineKeyboardMarkup(row_width=2)
for key, value in oy_buttons.items():
    oy_MB.insert(InlineKeyboardButton(text=key, callback_data=oy_callback.new(item_name=value)))
oy_MB.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_mb"))
oy_MB.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))


# Kunlik internet paketlar

kun_MB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 100 MB", callback_data="100mb_kun")
        ],
        [
            InlineKeyboardButton(text="🌐 300 MB", callback_data="300mb_kun")
        ],
        [
            InlineKeyboardButton(text="🌐 600 MB", callback_data="600mb_kun")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_mb"),
            InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob")
        ]
    ]
)

# Tungi internet paketlar

tun_MB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Tun", callback_data="tun")
        ],
        [
            InlineKeyboardButton(text="🌐 7 Tun", callback_data="7tun")
        ],
        [
            InlineKeyboardButton(text="🌐 30 Tun", callback_data="30tun")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_mb"),
            InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob")
        ]
    ]
)

tasix_MB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 TAS-IX 2 GB", callback_data="TAS-IX_2GB")
        ],
        [
            InlineKeyboardButton(text="🌐 TAS-IX 10 GB", callback_data="TAS-IX_10GB")
        ],
        [
            InlineKeyboardButton(text="🌐 TAS-IX 15 GB", callback_data="TAS-IX_15GB")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_mb"),
            InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob")
        ]
    ])

# Interenet NON-STOP paketlar

nonstop_button = {
    "3 000 MB NON-STOP": "non_stop3",
    "5 000 MB NON-STOP": "non_stop5",
    "8 000 MB NON-STOP": "non_stop8",
    "12 000 MB NON-STOP": "non_stop12",
    "16 000 MB NON-STOP": "non_stop16",
    "20 000 MB NON-STOP": "non_stop20",
    "30 000 MB NON-STOP": "non_stop30",
    "50 000 MB NON-STOP": "non_stop50",
}

non_stop = InlineKeyboardMarkup(row_width=2)
for key, value in nonstop_button.items():
    non_stop.insert(InlineKeyboardButton(text=key, callback_data=value))
non_stop.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_mb"))
non_stop.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))

# Ta'lim tarif rejasi uchun internet paketlar

talim_tr = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 5000 MB", callback_data="edu5")
        ],
        [
            InlineKeyboardButton(text="🌐 8000 M", callback_data="edu8")
        ],
        [
            InlineKeyboardButton(text="🌐 12 000 MB", callback_data="edu12")
        ],
        [
            InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_mb"),
            InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob")
        ]
    ])

# Daqiqa paketlari uchun tugmalar:
minute_buttons = {
    "📞 100 Daqiqa": "100daq",
    "📞 300 Daqiqa": "300daq",
    "📞 600 Daqiqa": "600daq",
    "📞 1200 Daqiqa": "1200daq",
}

daqiqa_menu = InlineKeyboardMarkup(row_width=2)
for key, value in minute_buttons.items():
    daqiqa_menu.insert(InlineKeyboardButton(text=key, callback_data=value))
daqiqa_menu.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob"))


# SMS paketlari uchun tugmalar:

sms_menu = InlineKeyboardMarkup(row_width=1)
sms_menu.insert(InlineKeyboardButton(text="✉️ Kunlik SMS paketlar", callback_data="SMS_Kun"))
sms_menu.insert(InlineKeyboardButton(text="✉️ Oylik SMS paketlar", callback_data="SMS_Oy"))
sms_menu.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob"))

# Kunlik SMS
sms_kun = InlineKeyboardMarkup(row_width=2)
sms_kun.insert(InlineKeyboardButton(text="✉️ 50 SMS", callback_data="SMSkun50"))
sms_kun.insert(InlineKeyboardButton(text="✉️ 100 SMS", callback_data="SMSkun100"))
sms_kun.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_sms"))
sms_kun.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))

# Oylik SMS

oy_sms_buttons = {
    "✉️ 10 SMS": "SMSoy10",
    "✉️ 50 SMS": "SMSoy50",
    "✉️ 200 SMS": "SMSoy200",
    "✉️ 500 SMS": "SMSoy500",
}

sms_oy = InlineKeyboardMarkup(row_width=2)
for key, value in oy_sms_buttons.items():
    sms_oy.insert(InlineKeyboardButton(text=key, callback_data=value))
sms_oy.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob_sms"))
sms_oy.insert(InlineKeyboardButton(text="🏠 Bosh sahifaga", callback_data="home_uzmob"))

# USSD menu kodlari
ussd_menu = InlineKeyboardMarkup(row_width=1)
ussd_menu.insert(InlineKeyboardButton(text="👩🏻‍💻 Operator", callback_data="operator"))
ussd_menu.insert(InlineKeyboardButton(text="◀️ Ortga", callback_data="back_uzmob"))

