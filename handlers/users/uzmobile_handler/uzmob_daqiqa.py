from aiogram.types import CallbackQuery
from keyboards.inline.menuUzmob import daqiqa_menu
from loader import dp

@dp.callback_query_handler(text=('100daq'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🕕Daqiqa to'plamlar

⏱ 100 Daqiqa
💳 To'plam narxi: 4000 so'm
📲 Faollashtirish: *111*2*3*1#

⏱ Amal qilish muddati: 30 kun""", reply_markup=daqiqa_menu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text=('300daq'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🕕Daqiqa to'plamlar

⏱ 300 Daqiqa
💳 To'plam narxi: 10000 so'm
📲 Faollashtirish: *111*2*3*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=daqiqa_menu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text=('600daq'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🕕Daqiqa to'plamlar

⏱ 600 Daqiqa
💳 To'plam narxi: 16000 so'm
📲 Faollashtirish: *111*2*3*3#

⏱ Amal qilish muddati: 30 kun""", reply_markup=daqiqa_menu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('1200daq'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🕕Daqiqa to'plamlar

⏱ 1200 Daqiqa
💳 To'plam narxi: 24000 so'm
📲 Faollashtirish: *111*2*3*4#

⏱ Amal qilish muddati: 30 kun""", reply_markup=daqiqa_menu)
    await call.answer(cache_time=60)

