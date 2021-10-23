from aiogram.types import CallbackQuery
from keyboards.inline.menuMobiuz import mobiuz, services, tarif_menu, net_menu, daqiqa_menu, sms_menu, ussd_menu
from loader import dp

@dp.callback_query_handler(text=('mobiTarif'))
async def tariflar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mobiuz aloqa operotorining tarif rejalari:", reply_markup=tarif_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('mobiXizmat'))
async def xizmatlar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mobiuz aloqa operotorining xizmatlari:", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('mobiInternet'))
async def internet(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mobiuz aloqa operotorining internet paketlari:", reply_markup=net_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('mobiDaqiqa'))
async def daqiqalar(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mobiuz aloqa operotorining daqiqa paketlari:", reply_markup=daqiqa_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('mobiSMS'))
async def sms(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mobiuz aloqa operotorining SMS paketlari:", reply_markup=sms_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('mobiUSSD'))
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

@dp.callback_query_handler(text=("back_mobiuz"))
async def back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mobiuz aloq operatorining tarif, xizmat, paket va USSD kodlari:", reply_markup=mobiuz)
    await call.answer(cache_time=60)

# Tariflar menyusi
@dp.callback_query_handler(text=("back_tarif"))
async def backtarif(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mobiuz aloqa operatorining tariflari:", reply_markup=tarif_menu)
    await call.answer(cache_time=60)