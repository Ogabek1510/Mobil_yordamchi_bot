from aiogram.types import CallbackQuery
from keyboards.inline.menuUzmob import oy_MB, kun_MB, tun_MB, tasix_MB, talim_tr, non_stop
from keyboards.inline.callback_uzmob import net_callback, oy_callback
from loader import dp

### Internet paketlar

@dp.callback_query_handler(net_callback.filter(item_name="MB_Oy"))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('🌐 Oylik internet paketlar', reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(net_callback.filter(item_name='MB_Kun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('🌐 Kunlik internet paketlar', reply_markup=kun_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(net_callback.filter(item_name='MB_Tun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('🌐 Tungi internet paketlar', reply_markup=tun_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(net_callback.filter(item_name='MB_TAS-IX'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('🌐 TAS-IX internet paketlar', reply_markup=tasix_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(net_callback.filter(item_name='non-stop'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('🌐 NON-STOP internet paketlar', reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(net_callback.filter(item_name='MB_Talim'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('<b>🌐 "Ta\'lim" tarif rejasi uchun maxsus internet paketlar</b>', reply_markup=talim_tr)
    await call.answer(cache_time=60)

# Oylik internet paketlar


@dp.callback_query_handler(oy_callback.filter(item_name="500mb_oy"))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Oylik internet paketlar</b>

💠 500 MB
<b>💵 To'plam narxi:</b> 10 000 so'm
<b>📲 Faollashtirish:</b> <code>*147*10072*72642#</code>

<b>⏱ Amal qilish muddati:</b> 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='1500mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Oylik internet paketlar</b>

💠 1 500 MB
<b>💵 To'plam narxi:</b> 15 000 so'm
<b>📲 Faollashtirish:</b> <code>*147*10073*72642#</code>

<b>⏱ Amal qilish muddati:</b> 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='3000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🌐 Oylik internet paketlar

💠 3 000 MB
💵 To'plam narxi: 24 000 so'm
📲 Faollashtirish: *147*10074*72642#

⏱ Amal qilish muddati: 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='5000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Oylik internet paketlar</b>

💠 5 000 MB
<b>💵 To'plam narxi:</b> 32 000 so'm
<b>📲 Faollashtirish:</b> *147*10075*72642#

<b>⏱ Amal qilish muddati:</b> 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='8000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Oylik internet paketlar</b>

💠 8 000 MB
<b>💵 To'plam narxi:</b> 41 000 so'm
<b>📲 Faollashtirish:</b> <code>*147*10076*72642#</code>

⏱ Amal qilish muddati: 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='12000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🌐 Oylik internet paketlar

💠 12 000 MB
💵 To'plam narxi: 50 000 so'm
📲 Faollashtirish: *147*10077*72642#

⏱ Amal qilish muddati: 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='20000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🌐 Oylik internet paketlar

💠 20 000 MB
💵 To'plam narxi: 65 000 so'm
📲 Faollashtirish: *147*10078*72642#

⏱ Amal qilish muddati: 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='30000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🌐 Oylik internet paketlar

💠 30 000 MB
💵 To'plam narxi: 75 000 so'm
📲 Faollashtirish: *147*10079*72642#

⏱ Amal qilish muddati: 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='50000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🌐 Oylik internet paketlar

💠 50 000 MB
💵 To'plam narxi: 85 000 so'm
📲 Faollashtirish: *147*10080*72642#

⏱ Amal qilish muddati: 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(oy_callback.filter(item_name='75000mb'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🌐 Oylik internet paketlar

💠 75 000 MB
💵 To'plam narxi: 110 000 so'm
📲 Faollashtirish: *147*10150*72642#

⏱ Amal qilish muddati: 30 kun""", reply_markup=oy_MB)
    await call.answer(cache_time=60)

# Kunlik internet paketlar

@dp.callback_query_handler(text=('100mb_kun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Kunlik internet paketlar</b>

💠 100 MB
💵 To'plam narxi: 3 000 so'm
📲 Faollashtirish: *147*10043*72642#

⏱ Amal qilish muddati: 1 kun""", reply_markup=kun_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('300mb_kun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Kunlik internet paketlar</b>
💠 300 MB
💵 To'plam narxi: 6 000 so'm
📲 Faollashtirish: *147*10050*72642#

⏱ Amal qilish muddati: 1 kun""", reply_markup=kun_MB)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text=('600mb_kun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Kunlik internet paketlar</b>
💠 600 MB
💵 To'plam narxi: 9 000 so'm
📲 Faollashtirish: *147*10051*72642#

⏱ Amal qilish muddati: 1 kun""", reply_markup=kun_MB)
    await call.answer(cache_time=60)

# Tungi internet paket

@dp.callback_query_handler(text=('tun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Tungi internet paketlar</b>
💠 12 000 MB
💵 To'plam narxi: 6 300 so'm
📲 Faollashtirish: *111*2*18*1#

⏱ Amal qilish muddati: 1 tun (01:00 - 07:59)""", reply_markup=tun_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('7tun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Tungi internet paketlar</b>
💠 31 500 MB
💵 To'plam narxi: 12 000 so'm
📲 Faollashtirish: *111*2*18*3#

⏱ Amal qilish muddati: 7 tun (01:00 - 07:59)""", reply_markup=tun_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('30tun'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 Tungi internet paketlar</b>
💠 12 000 MB
💵 To'plam narxi: 99 000 so'm
📲 Faollashtirish: *111*2*18*2#

⏱ Amal qilish muddati: 30 tun (01:00 - 07:59)""", reply_markup=tun_MB)
    await call.answer(cache_time=60)

# TAS-IX internet paketlar

@dp.callback_query_handler(text=('TAS-IX_2GB'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 TAS-IX internet paketlar</b>
💠 2 480 MB
<b>💵  To'plam narxi:</b> 15 000 so'm
<b>📲 Faollashtirish:</b> <code>*147*10068*72642#</code>

<b>⏱ Amal qilish muddati:</b> 90 kun""", reply_markup=tasix_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('TAS-IX_10GB'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 TAS-IX internet paketlar</b>
💠 10 240 MB
<b>💵  To'plam narxi:</b> 40 000 so'm
<b>📲 Faollashtirish:</b> <code>*147*10069*72642#</code>

<b>⏱ Amal qilish muddati:</b> 90 kun""", reply_markup=tasix_MB)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('TAS-IX_15GB'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 TAS-IX internet paketlar</b>
💠 15 360 MB
<b>💵  To'plam narxi:</b> 50 000 so'm
<b>📲 Faollashtirish:</b> <code>*147*10070*72642#</code>

<b>⏱ Amal qilish muddati:</b> 90 kun""", reply_markup=tasix_MB)
    await call.answer(cache_time=60)

# Internet NON-STOP paketlar

@dp.callback_query_handler(text=('non_stop3'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 3000 MB
💳 To'plam narxi: 24000 so'm ikkinchi va keyingi oylardagi narxi: 21600 so'm
✅ Faollashtirish: *147*10055*28585# 
❎O'chirish: *111*1*14*1*2#


⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('non_stop5'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 5000 MB
💳 To'plam narxi: 32000 so'm ikkinchi va keyingi oylardagi narxi: 28800 so'm
✅ Faollashtirish: *147*10056*28585# 
❎O'chirish: *111*1*14*2*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('non_stop8'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 8000 MB
💳 To'plam narxi: 41000 so'm ikkinchi va keyingi oylardagi narxi: 36900 so'm
✅ Faollashtirish: *147*10057*28585# 
❎O'chirish: *111*1*14*3*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('non_stop12'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 12000 MB
💳 To'plam narxi: 50000 so'm ikkinchi va keyingi oylardagi narxi: 45000 so'm
✅ Faollashtirish: *147*10151*28585# 
❎O'chirish: *111*1*14*4*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('non_stop16'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 16 000 MB
💳 To'plam narxi: 60 000 so'm ikkinchi va keyingi oylardagi narxi: 54 000 so'm
✅ Faollashtirish: *111*1*14*9*1# 
❎O'chirish: *111*1*14*9*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('non_stop20'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 20000 MB
💳 To'plam narxi: 65000 so'm ikkinchi va keyingi oylardagi narxi: 58500 so'm
✅ Faollashtirish: *147*10152*28585# 
❎O'chirish: *111*1*14*5*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('non_stop30'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 30000 MB
💳 To'plam narxi: 75000 so'm ikkinchi va keyingi oylardagi narxi: 67500 so'm
✅ Faollashtirish: *147*10153*28585# 
❎O'chirish: *111*1*14*6*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('non_stop50'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔴Internet Non-stop

💠 50000 MB
💳 To'plam narxi: 85000 so'm ikkinchi va keyingi oylardagi narxi: 76500 so'm
✅ Faollashtirish: *147*10154*28585# 
❎O'chirish: *111*1*14*7*2#

⏱ Amal qilish muddati: 30 kun""", reply_markup=non_stop)
    await call.answer(cache_time=60)

# Ta'lim tarif rejasi uchun internet paketlar

@dp.callback_query_handler(text=('edu5'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 "Ta'lim" tarif rejasi uchun maxsus internet paketlar</b>
💠 5 000 MB
<b>💵  To'plam narxi:</b> 26 600 so'm
<b>📲 Faollashtirish:</b> <code>*255*1*1#</code>

<b>⏱ Amal qilish muddati:</b> 30 kun""", reply_markup=talim_tr)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('edu8'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 "Ta'lim" tarif rejasi uchun maxsus internet paketlar</b>
💠 8 000 MB
<b>💵  To'plam narxi:</b> 32 800 so'm
<b>📲 Faollashtirish:</b> <code>*255*1*2#</code>

<b>⏱ Amal qilish muddati:</b> 30 kun""", reply_markup=talim_tr)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text=('edu12'))
async def oy_mb(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌐 "Ta'lim" tarif rejasi uchun maxsus internet paketlar</b>
💠 8 000 MB
<b>💵  To'plam narxi:</b> 32 800 so'm
<b>📲 Faollashtirish:</b> <code>*255*1*2#</code>

<b>⏱ Amal qilish muddati:</b> 30 kun""", reply_markup=talim_tr)
    await call.answer(cache_time=60)

