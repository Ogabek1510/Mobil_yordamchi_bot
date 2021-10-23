from aiogram.types import CallbackQuery
from keyboards.inline.menuUzmob import uzmob, tarif_menu, services, net_menu, daqiqa_menu, sms_menu, ussd_menu
from loader import dp

@dp.callback_query_handler(text_contains=('UzmobiTarif'))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Tarif reja turini tanlang</b>", reply_markup=tarif_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=('UzmobiXizmat'))
async def xizmatlar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Uzmobile aloqa operatorining xizmatlari:</b>", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=('UzmobiInternet'))
async def internet(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Uzmobile aloqa operotorining internet paketlari:</b>", reply_markup=net_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=('UzmobiDaqiqa'))
async def daqiqa(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Uzmobile aloqa operotorining daqiqa paketlari:</b>", reply_markup=daqiqa_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=('UzmobiSMS'))
async def sms(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Uzmobile aloqa operotorining SMS paketlari:</b>", reply_markup=sms_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=('UzmobiUSSD'))
async def ussd(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔹 *105# - Limit qoldig'i va balansni tekshirish
➖➖➖➖➖➖➖➖➖➖➖➖
🔹 *100*4# - Mening raqamim
➖➖➖➖➖➖➖➖➖➖➖➖
🔹 *100*2# - Qolgan vaqt, internet va sms limiti haqida ma'lumot
➖➖➖➖➖➖➖➖➖➖➖➖
🔹*555# - "Restart" xizmatini muvaffaqiyatli faollashtirganda
➖➖➖➖➖➖➖➖➖➖➖➖
🔹*150# - Extra balans (Qarz olish)
➖➖➖➖➖➖➖➖➖➖➖➖
🔹 *100*5# - Mening raqamlarim
➖➖➖➖➖➖➖➖➖➖➖➖
🔹*100*6# - Mening raqamlarim qoldig'i
➖➖➖➖➖➖➖➖➖➖➖➖
🔹 *111*2*7*1# 4G LTE ni yoqish
➖➖➖➖➖➖➖➖➖➖➖➖
🔹 *111*2*7*2# 4G LTE ni o'chirish
➖➖➖➖➖➖➖➖➖➖➖➖
🔹 *43# - Kutib turishni faollashtirish
➖➖➖➖➖➖➖➖➖➖➖➖
🔹 *#67# - Pereadrisatsiyani tekshirish""", reply_markup=ussd_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=("operator"))
async def back(call: CallbackQuery):
    await call.answer("☎️ Call center  - 1099", cache_time=60, show_alert=True)

# Ortga qaytish tugmalari

@dp.callback_query_handler(text=("back_uzmob"))
async def back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🔵 Uzmobile aloq operatorining tarif, xizmat, paket va USSD kodlari:</b>", reply_markup=uzmob)
    await call.answer()

@dp.callback_query_handler(text=("back_uzmob_tarif"))
async def back_tarif(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Tarif reja turini tanlang</b>", reply_markup=tarif_menu)
    await call.answer()

@dp.callback_query_handler(text=("home_uzmob"))
async def home(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>🔵 Uzmobile aloq operatorining tarif, xizmat, paket va USSD kodlari:</b>", reply_markup=uzmob)
    await call.answer()

@dp.callback_query_handler(text=("back_uzmob_mb"))
async def home(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Uzmobile aloqa operotorining internet paketlari:</b>", reply_markup=net_menu)
    await call.answer()

