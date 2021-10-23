from aiogram.types import CallbackQuery
from keyboards.inline.menuUcell import ucell, tarif_menu, net_menu, daqiqa_menu, sms_menu, ussd_menu
from loader import dp

@dp.callback_query_handler(text=('ucellTarif'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ucell aloqa operotorining tarif rejalari:", reply_markup=tarif_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('ucellInternet'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ucell aloqa operotorining internet paketlari:", reply_markup=net_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('ucellDaqiqa'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ucell aloqa operotorining daqiqa paketlari:", reply_markup=daqiqa_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('ucellSMS'))
async def net(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ucell aloqa operotorining SMS paketlari:", reply_markup=sms_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('ucellUSSD'))
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
🔹 *#67# - Pereadrisatsiyani tekshirish""", reply_markup=ussd_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=("back_ucell"))
async def back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ucell aloq operatorining tarif, xizmat, paket va USSD kodlari:", reply_markup=ucell)
    await call.answer(cache_time=60)