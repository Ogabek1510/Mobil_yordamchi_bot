from aiogram.types import CallbackQuery
from keyboards.inline.menuBeeline import tarif
from loader import dp

@dp.callback_query_handler(text_contains=("zor3"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""ZO'R 3
USSD orqali ulanish *2*3#

Oylik abonent to’lovi: 20000 so'm
O'zbekiston bo'yicha daqiqalar *: 1500 min
Internet barcha yo’nalishlarga: 3 GB
O'zbekiston bo'yicha SMS: 1500 
Balansingizda bir oylik abonent to’lovini yechish uchun yetarli mablag’ bo’lmaganda:
Kunlik abonent to’lovi: 2000 so'm
O'zbekiston bo'yicha daqiqalar *: 100 min
O'zbekiston bo'yicha SMS: 100 
Internet barcha yo’nalishlarga: 100 MB
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori (tarifga o'tish narxini hisobga olmagan holda): 20250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("zor5"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""ZO'R 5
USSD orqali ulanish *2*5#

Oylik abonent to’lovi: 27000 so'm
O'zbekiston bo'yicha daqiqalar *: 2500 min
Internet barcha yo’nalishlarga: 5 GB
O'zbekiston bo'yicha SMS: 2500 
Balansingizda bir oylik abonent to’lovini yechish uchun yetarli mablag’ bo’lmaganda:
Kunlik abonent to’lovi: 2000 so'm
O'zbekiston bo'yicha daqiqalar *: 100 min
O'zbekiston bo'yicha SMS: 100 
Internet barcha yo’nalishlarga: 100 MB
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori (tarifga o'tish narxini hisobga olmagan holda): 27250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("zor7"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""ZO'R 7
USSD orqali ulanish *2*7#

Oylik abonent to’lovi: 35000 so'm
O'zbekiston bo'ylab cheksiz qo'ng'iroqlar *
Internet barcha yo’nalishlarga: 7 GB
O'zbekiston bo'yicha SMS: 5000 
Balansingizda bir oylik abonent to’lovini yechish uchun yetarli mablag’ bo’lmaganda:
Kunlik abonent to’lovi: 2000 so'm
O'zbekiston bo'yicha daqiqalar *: 100 min
O'zbekiston bo'yicha SMS: 100 
Internet barcha yo’nalishlarga: 100 MB
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori (tarifga o'tish narxini hisobga olmagan holda): 35250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("zor12"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""ZO'R 12
USSD orqali ulanish *2*12#

Oylik abonent to’lovi: 50000 so'm
O'zbekiston bo'ylab cheksiz qo'ng'iroqlar *
Internet barcha yo’nalishlarga: 12 GB
O'zbekiston bo'yicha SMS: 5000 
Balansingizda bir oylik abonent to’lovini yechish uchun yetarli mablag’ bo’lmaganda:
Kunlik abonent to’lovi: 2000 so'm
O'zbekiston bo'yicha daqiqalar *: 100 min
O'zbekiston bo'yicha SMS: 100 
Internet barcha yo’nalishlarga: 100 MB
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori (tarifga o'tish narxini hisobga olmagan holda): 50250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("zor20"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""ZO'R 20
USSD orqali ulanish *2*20#

Oylik abonent to’lovi: 70000 so'm
O'zbekiston bo'ylab cheksiz qo'ng'iroqlar *
Internet barcha yo’nalishlarga: 20 GB
O'zbekiston bo'yicha SMS: 5000 
Balansingizda bir oylik abonent to’lovini yechish uchun yetarli mablag’ bo’lmaganda:
Kunlik abonent to’lovi: 2000 so'm
O'zbekiston bo'yicha daqiqalar *: 100 min
O'zbekiston bo'yicha SMS: 100 
Internet barcha yo’nalishlarga: 100 MB
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori (tarifga o'tish narxini hisobga olmagan holda): 70250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("status_silver"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""Status Silver
USSD orqali ulanish *2*30#

Oylik abonent to’lovi: 90000 so'm
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori: 90250 so'm
O'zbekiston bo'ylab cheksiz qo'ng'iroqlar *
GB paketi: 30 GB
O'zbekiston bo'yicha SMS paketi: 5000 
Roumingda VEON hududi uchun kiritilgan MB paketi**: 100 MB
Bepul «Oltin» raqam: 210500 so'm
Bepul yoqtirilgan xizmat - «Xabardor bo’l»: 0 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("starus_gold"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""Status Gold
USSD orqali ulanish *2*50#

Oylik abonent to’lovi: 130000 so'm
O'zbekiston bo'ylab cheksiz qo'ng'iroqlar *
GB paketi: 50 GB
O'zbekiston bo'yicha SMS paketi: 10000 
Roumingda VEON hududida kirish/chiqish qo’ng’iroqlari uchun daqiqalar paketi**: 50 min
Roumingda VEON hududida foydalanish uchun kiritilgan MB paketi**: 250 MB
Roumingda VEON hududida kiruvchi qo’ng’iroqlarga chegirma: 50 
Bepul «Oltin» raqam: 421000 so'm
Bepul yoqtirilgan xizmatlar - «Xabardor bo’l», «AntiAON»: 0 so'm
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori: 130250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("status_platinu"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""Status Platinum
USSD orqali ulanish *2*150#

Oylik abonent to’lovi: 200000 so'm
O'zbekiston bo'ylab cheksiz qo'ng'iroqlar *
GB paketi: 150 GB
O'zbekiston bo'yicha SMS paketi: 10000 
Roumingda VEON hududida kirish/chiqish qo’ng’iroqlari uchun daqiqalar paketi**: 100 min
Roumingda VEON hududida foydalanish uchun kiritilgan MB paketi**: 500 MB
Barcha xalqaro qo'ng'iroqlar uchun kiritilgan daqiqalar paketi: 100 min
Bepul «Oltin» raqam: 1263000 so'm
Bepul yoqtirilgan xizmatlar - «Xabardor bo’l», «AntiAON»: 0 so'm
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori: 189250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("oson1"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""OSON 1
Подключить по USSD *2*01#

Oylik abonent to’lovi: 40000 so'm
O'zbekiston bo'ylab cheksiz qo'ng'iroqlar *: 9999999999 min
Internet, 1 MB: 1 so'm
O’zbekiston bo’yicha 1 SMS: 1 so'm
Tarifga o'tish uchun hisobdagi minimal mablag’ miqdori: 40250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("oson10"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""OSON 10
Подключить по USSD *110*61#

Oylik abonent to’lovi: 10000 so'm
O'zbekiston bo'yicha daqiqalar paketi: 10 min
O'zbekiston bo'yicha SMS paketi: 10 
Internet, MB: 10 MB
Mavjud abonentlarga tarifga o'tish uchun hisobdagi minimal mablag’ miqdori: 10250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("allo"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""ALLO
USSD orqali ulanish *110*40#

Oylik abonent to’lovi: 15000 so'm
O'zbekiston bo'yicha daqiqalar paketi *: 600 min
O'zbekiston bo'yicha SMS paketi: 600 
Kunlik abonent to’lovi: 600 so'm
O'zbekiston bo'yicha daqiqalar paketi: 20 min
O'zbekiston bo'yicha SMS paketi: 20 
Mavjud abonentlarga tarifga o'tish uchun hisobdagi minimal mablag’ miqdori: 15250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("status_platinu"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("kunlik"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""Kunlik
USSD orqali ulanish *110*580#

Kunlik abonent to'lovi: 600 so'm
O'zbekiston bo'ylab kiritilgan chiqish qo'ng'iroqlari *: 60 min
Barcha yo'nalishga kiritilgan megabayt: 60 MB
Cashback*: 10 
Barcha kirish qo'ng'iroqlari: 0 so'm
O'zbekiston bo'yicha chiquvchi qo'ng'iroqlar: 100 so'm
Internet, 1 MB: 100 so'm
O‘zbekiston bo‘yicha chiquvchi SMS: 100 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("click+"))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text="""Click+
USSD orqali ulanish *110*22#

Barcha yo'nalishlar uchun MB paketi: 1 GB
Facebook, Odnoklassniki, TAS-IX, Telegram, WhatsApp va Viber uchun MB paketi: 1 GB
«TAS-IX» hududiga kiradigan saytlar uchun MB paketi: 1 GB
Tarif rejasida ovozli aloqa xizmati taqdim etilmaydi
Internet, 1 MB: 25 so'm
O'zbekiston bo'ylab SMS-xabarni yuborish: 85 so'm
Xalqaro SMS-xabarni yuborish: 500 so'm
Ulanish uchun hisobdagi minimal mablag’ miqdori: 15250 so'm""", reply_markup=tarif)
    await call.answer(cache_time=60)