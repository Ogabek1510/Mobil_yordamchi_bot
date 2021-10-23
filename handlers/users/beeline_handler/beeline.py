from aiogram.types import CallbackQuery
from keyboards.inline.menuBeeline import beeline, tarif, netpaket, daqiqa, sms, ussd
from loader import dp

@dp.callback_query_handler(text_contains=('beelineTarif'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Beeline aloqa operotorining tarif rejalari:", reply_markup=tarif)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('beelineInternet'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Beeline aloqa operotorining internet paketlari:", reply_markup=netpaket)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('beelineDaqiqa'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Beeline aloqa operotorining daqiqa paketlari:", reply_markup=daqiqa)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('beelineSMS'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Beeline aloqa operotorining SMS paketlari:", reply_markup=sms)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('beelineUSSD'))
async def net(call: CallbackQuery):
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
🔹 *#67# - Pereadrisatsiyani tekshirish""", reply_markup=ussd)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=("back_beeline"))
async def back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Beeline aloq operatorining tarif, xizmat, paket va USSD kodlari:", reply_markup=beeline)
    await call.answer(cache_time=60)