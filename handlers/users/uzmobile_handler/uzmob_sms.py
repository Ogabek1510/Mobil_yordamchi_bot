from aiogram.types import CallbackQuery
from keyboards.inline.menuUzmob import sms_menu, sms_kun, sms_oy
from loader import dp

@dp.callback_query_handler(text='SMS_Kun')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kunlik SMS paketlar", reply_markup=sms_kun)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='SMS_Oy')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Oylik SMS paketlar", reply_markup=sms_oy)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='back_uzmob_sms')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("<b>Uzmobile aloqa operotorining SMS paketlari:</b>", reply_markup=sms_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='SMSkun50')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""📨Kunlik SMS paketlar

📩50 SMS
💰Narxi 420 so'm
💵Kunlik abonent to'lovi 420 so'm
⚖️Berilgan smslar soni: 50 
🧭Amal qilish muddati 1 kun
✅Faollashtirish: *111*2*19*1*1#
❎O‘chirish: *111*1*19*1*2#""", reply_markup=sms_kun)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='SMSkun100')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""📨Kunlik SMS paketlar

📩100 SMS
💰Narxi 840 so'm
💵Kunlik abonent to'lovi 840 so'm
⚖️Berilgan smslar soni: 100 
🧭Amal qilish muddati 1 kun
✅Faollashtirish: *111*2*19*2*1#
❎O‘chirish: *111*1*19*2*2#""", reply_markup=sms_kun)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='SMSoy10')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""📨Oylik SMS paketlar

📩 10 SMS
💳 To'plam narxi: 420 so'm
📲 Faollashtirish: *111*2*1*1#
🧭Amal qilish muddati: 30 kun""", reply_markup=sms_oy)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='SMSoy50')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""📨Oylik SMS paketlar

📩 50 SMS
💳 To'plam narxi: 1680 so'm
📲 Faollashtirish: *111*2*1*2#
🧭Amal qilish muddati: 30 kun""", reply_markup=sms_oy)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='SMSoy200')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""📨Oylik SMS paketlar

📩 200 SMS
💳 To'plam narxi: 5200 so'm
📲 Faollashtirish: *111*2*1*3#
🧭Amal qilish muddati: 30 kun""", reply_markup=sms_oy)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text='SMSoy500')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""📨Oylik SMS paketlar

📩 500 SMS
💳 To'plam narxi: 9500 so'm
📲 Faollashtirish: *111*2*1*4#
🧭Amal qilish muddati: 30 kun""", reply_markup=sms_oy)
    await call.answer(cache_time=60)