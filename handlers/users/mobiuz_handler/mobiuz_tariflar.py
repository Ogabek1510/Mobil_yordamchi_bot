from aiogram.types import CallbackQuery
from keyboards.inline.menuMobiuz import mobi, for_net, annual
from loader import dp

### Tariflar menyusi

@dp.callback_query_handler(text=("Mobi"))
async def _mobi(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uzmobile aloq operatorining Mobi turkumidagi tarif rejalari", reply_markup=mobi)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=("fornet"))
async def fornet(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uzmobile aloq operatorining Mobi turkumidagi tarif rejalari", reply_markup=for_net)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=("annual"))
async def yillik(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uzmobile aloq operatorining Mobi turkumidagi tarif rejalari", reply_markup=annual)
    await call.answer(cache_time=60)

