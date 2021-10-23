from aiogram.types import CallbackQuery
from keyboards.inline.menuUzmob import activ, privil, units
from keyboards.inline.callback_uzmob import privil_callback
from loader import dp

### Tariflar menyusi

@dp.callback_query_handler(text_contains=("Faol"))
async def faol(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uzmobile aloq operatorining faol tarif rejalari", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Imtiyoz"))
async def imtiyozli(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uzmobile aloq operatorining imtiyozli tarif rejalari:", reply_markup=privil)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Units"))
async def _units_(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uzmobile aloq operatorining Units turkumidagi tarif rejalari:", reply_markup=units)
    await call.answer(cache_time=60)


# Faol tariflar

@dp.callback_query_handler(text_contains=("Oddiy10"))
async def faol_oddiy(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Oddiy 10" tarif rejasi

Abonent toʻlovi oyiga 10000 soʻm 
Oʻzbekiston boʻyicha chiquvchi 10 daqiqa 
Mobil internet 10 MB 
Oʻzbekiston boʻyicha 10 SMS 

Oʻzbekiston boʻyicha qoʻngʻiroqlar: 10 soʻm (limitdan tashqari) 
1 MB internet trafik: 10 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 10 soʻm (limitdan tashqari) 

Tarif rejasiga oʻtish narxi 10 000 soʻm 
Tarif almashtirish: *111*1*11*12#""", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Street"))
async def faol_street(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Street" tarif rejasi

Abonent to'lovi oyiga 39900 so'm 
O'zbekiston bo'yicha 750 daqiqa 
Tarmoq ichida 1500 daqiqa 
Mobil internet 6500 MB  
O'zbekiston bo'yicha 750 SMS 

O'zbekiston bo'yicha daqiqa: 126 soʻm (limitdan tashqari) 
1 MB internet trafik: 160 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 84 soʻm (limitdan tashqari) 

Tarif oʻzgartirish: *111*1*11*1*1#""", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Onlime"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Onlime" (New) tarif rejasi

Abonent to'lovi oyiga 49900 so'm 
O'zbekiston bo'yicha 1000 daqiqa 
Tarmoq ichida 2000 daqiqa 
Mobil internet 10000 MB  
O'zbekiston bo'yicha 1000 SMS 

O'zbekiston bo'yicha daqiqa: 84 soʻm (limitdan tashqari) 
1 MB internet trafik: 280 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 84 soʻm (limitdan tashqari) 

Tarif oʻzgartirish: *111*1*11*6#""", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Flash"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Flash" tarif rejasi

Abonent to'lovi oyiga 69900 so'm 
O'zbekiston bo'yicha 1500 daqiqa 
Tarmoq ichida 2000 daqiqa 
Mobil internet 16000 MB  
O'zbekiston bo'yicha 1500 SMS 

O'zbekiston bo'yicha daqiqa: 84 soʻm (limitdan tashqari) 
1 MB internet trafik: 160 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 84 soʻm (limitdan tashqari) 

Tarif oʻzgartirish: *111*1*11*2*1#""", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Ishbil"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Ishbilarmon" tarif rejasi

Abonent toʻlovi oyiga 99 000 soʻm 
Oʻzbekiston boʻyicha daqiqalar CHEKSIZ. 
Mobil internet trafik 25 000 MB. 
Oʻzbekiston boʻyicha 3000 SMS. 

Tarif rejasiga oʻtish bepul 
Tarif almashtirish: *111*1*11*10#""", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("StreetUp"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Street UPGRADE" tarif rejasi

Abonent to'lovi 3 oyiga: 119 700 so'm 
O'zbekiston bo'yicha 3 oyiga: 3000 daqiqa 
Tarmoq ichida 3 oyiga: 6000 daqiqa 
Mobil internet 3 oyiga: 26000 MB  
O'zbekiston bo'yicha 3 oyiga: 3000 SMS 

O'zbekiston bo'yicha daqiqa: 126 soʻm (limitdan tashqari) 
1 MB internet trafik: 160 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 84 soʻm (limitdan tashqari) 

Tarif oʻzgartirish: *111*1*11*4*1#""", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Royal"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Royal" tarif rejasi

Abonent toʻlovi oyiga 149 900 soʻm 
Oʻzbekiston boʻyicha daqiqalar CHEKSIZ* 
Mobil internet trafik CHEKSIZ** 
Oʻzbekiston boʻyicha 5000 SMS. 

Tarif oʻzgartirish: *111*1*11*3*1#""", reply_markup=activ)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("FlashUp"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Flash UPGRADE" tarif rejasi

Abonent to'lovi 3 oyiga: 209 700 so'm 
O'zbekiston bo'yicha 3 oyiga: 6000 daqiqa 
Tarmoq ichida 3 oyiga: 8000 daqiqa 
Mobil internet 3 oyiga: 64000 MB  
O'zbekiston bo'yicha 3 oyiga: 6000 SMS 

O'zbekiston bo'yicha daqiqa: 84 soʻm (limitdan tashqari) 
1 MB internet trafik: 160 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 84 soʻm (limitdan tashqari) 

Tarif oʻzgartirish: *111*1*11*5*1#""", reply_markup=activ)
    await call.answer(cache_time=60)


# Imtiyozli tariflar

@dp.callback_query_handler(privil_callback.filter(item_name="Talim"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Ta'lim" tarif rejasi

Abonent to'lovi oyiga 34900 so'm 
O'zbekiston bo'yicha 300 daqiqa 
Tarif rejasi ichida 1000 daqiqa 
Mobil internet 8000 MB  
O'zbekiston bo'yicha 500 SMS 

O'zbekiston bo'yicha daqiqa: 40 soʻm (limitdan tashqari) 
1 MB internet trafik: 40 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 84 soʻm (limitdan tashqari) 

“TA‘LIM” tarif rejasi faqat oliy va o‘rta maxsus o‘quv yurtlari (institutlar, universitetlar, litseylar, kollejlar) talabalari va o‘qituvchilari uchun mo‘ljallangan. Ulanishda talabalar talabalik guvohnomasini va o‘qituvchilar esa guvohnomalarini taqdim etishlari kerak.""",
                              reply_markup=privil)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Maktab"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Maktab" tarif rejasi

Abonent to'lovi oyiga 29900 so'm 
O'zbekiston bo'yicha 200 daqiqa 
Tarif rejasi ichida 500 daqiqa 
Mobil internet 5000 MB  
O'zbekiston bo'yicha 500 SMS 

O'zbekiston bo'yicha daqiqa: 40 soʻm (limitdan tashqari) 
1 MB internet trafik: 40 soʻm (limitdan tashqari) 
Oʻzbekiston boʻylab SMS: 84 soʻm (limitdan tashqari) 

“MAKTAB” tarif rejasi maktab o‘quvchilari uchun mo‘ljallangan bo‘lib, xizmatni rasmiylashtirish ota-onalardan biriga bolaning tug‘ilganlik haqidagi guvohnomasi taqdim etilganda amalga oshiriladi.""",
                              reply_markup=privil)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Yoshlar"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Yoshlar" tarif rejasi

Abonent to'lovi oyiga 5000 so'm 
O'zbekiston bo'yicha chiquvchi qo'ng'iroqlar 25 so'm  
Tarmoq ichida chiquvchi qo'ng'iroqlar 25 so'm  
1 MB internet trafik narxi 25 so'm  
1 chiquvchi SMS narxi 25 so'm 

Tarif rejasiga boshqa tarif rejalaridan o‘tish mumkin emas.""",
                              reply_markup=privil)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("Bolajon"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Bolajon" tarif rejasi

Abonent toʻlovi oyiga 18000 soʻm 
Oʻzbekiston boʻyicha chiquvchi 200 daqiqa 
Mobil internet trafik 2000 MB* 
Oʻzbekiston boʻyicha 200 SMS  

* Trafik tarifikatsiyasi APN ziyonet.uzmobile.uz 
*Tarif bolalar uchun mo'ljallangan, ushbu tarifdagi raqamlar ota-onalardan biriga ulanadi.""",
                              reply_markup=privil)
    await call.answer(cache_time=60)

# Units tariflari
@dp.callback_query_handler(text_contains=("units700"))
async def units_700(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔵Uzmobile: "Units 700"

Abonent to'lovi 7 kunga 7000 so'm 
Kiritilgan limit 700 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 700 Unitlarni 700 MB uchun yoki 700 daqiqa so‘zlashish uchun foydalanish mumkin yoki 350 MB va 350 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*1#""", reply_markup=units)


@dp.callback_query_handler(text_contains=("units1500"))
async def units_1500(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Units 1500"

Abonent to'lovi 15 kunga 15000 so'm 
Kiritilgan limit 1500 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 1500 Unitlarni 1500 MB uchun yoki 1500 daqiqa so‘zlashish uchun foydalanish mumkin yoki 750 MB va 750 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*2#""", reply_markup=units)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("units4000"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Units 4000"

Abonent to'lovi 30 kunga 20000 so'm 
Kiritilgan limit 4000 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 3500 Unitlarni 3500 MB uchun yoki 3500 daqiqa so‘zlashish uchun foydalanish mumkin yoki 1750 MB va 1750 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*3#""", reply_markup=units)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("units8000"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(""""Units 8000"

Abonent to'lovi 30 kunga 35000 so'm 
Kiritilgan limit 8000 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 7000 Unitlarni 7000 MB uchun yoki 7000 daqiqa so‘zlashish uchun foydalanish mumkin yoki 3500 MB va 3500 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*4#""", reply_markup=units)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("units11000"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔵Uzmobile: "Units 11 000"

Abonent to'lovi 30 kunga 45000 so'm 
Kiritilgan limit 11000 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 10000 Unitlarni 10000 MB uchun yoki 10000 daqiqa so‘zlashish uchun foydalanish mumkin yoki 5000 MB va 5000 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*5#""", reply_markup=units)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("units14000"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔵Uzmobile: "Units 14 000"

Abonent to'lovi 30 kunga 55000 so'm 
Kiritilgan limit 14000 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 13000 Unitlarni 13000 MB uchun yoki 13000 daqiqa so‘zlashish uchun foydalanish mumkin yoki 6500 MB va 6500 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*6#""", reply_markup=units)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains=("units18000"))
async def faol_onlime(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔵Uzmobile: "Units 18 000"

Abonent to'lovi 30 kunga 65000 so'm 
Kiritilgan limit 18000 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 17000 Unitlarni 17000 MB uchun yoki 17000 daqiqa so‘zlashish uchun foydalanish mumkin yoki 8500 MB va 8500 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*7#""", reply_markup=units)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains=("units22000"))
async def un(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""🔵Uzmobile: "Units 22 000"

Abonent to'lovi 30 kunga 75000 so'm 
Kiritilgan limit 22000 Units 
O'zbekiston bo'yicha 1 daqiqa = 1 Unit 
Mobil internet 1 MB = 1 Unit 
O'zbekiston bo'yicha 1 SMS = 1 Unit 
 
Yaʼni berilgan Unitlarni ehtiyojga qarab istalgan shaklda sarflash mumkin. 
Misol: 21000 Unitlarni 21000 MB uchun yoki 21000 daqiqa so‘zlashish uchun foydalanish mumkin yoki 10500 MB va 10500 daqiqa uchun. 
Eslatma: "Units" tarif rejalarida oylik internet paketlar xarid qilib bo‘lmaydi va berilgan Unitlar tugagandan so‘ng hisobdagi mablag‘ orqali so‘zlashib bo‘lmaydi tarif rejasi bo‘yicha abonent to‘lovi to‘lab Restart (*555#) xizmatini faollashtirish mumkin. 
 
Tarif oʻzgartirish: *777*8#""", reply_markup=units)
    await call.answer(cache_time=60)



