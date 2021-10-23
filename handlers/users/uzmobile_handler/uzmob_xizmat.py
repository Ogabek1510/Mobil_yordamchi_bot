from aiogram.types import CallbackQuery
from keyboards.inline.menuUzmob import services
from loader import dp

@dp.callback_query_handler(text_contains='tarmoqda')
async def online (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>📲“Qabul qilinmagan qoʻngʻiroq“</b> va <b>“Tarmoqda”</b>

Endi Uzmobile GSM abonentlari "Qabul qilinmagan qo'ng'iroq" xizmati orqali telefoni o'chiq bo'lganda yoki tarmoqdan tashqari bo'lgan hollarda qabul qilinmagan qo'ng'iroqlar haqida ma'lumotga ega bo'lishlari mumkin

Xizmat abonent to‘lovi 40 so‘m kuniga

Faollashtirish *111*2*4*1#
Xizmatni o’chirish *111*2*4*2#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='4G')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>📶LTE (4G)</b>

Uzmobile Interneti ortiqcha harajatsiz 4G LTE tezligida!

Oʻta yuqori tezlik yordamida xohlagan joyingizda bilimingizni oshiring, hissiyotlaringiz bilan boʻlishing, faolroq suhbatlashing!

70 Mbit/sgacha tezlik nafaqat katta hajmdagi fayllarni koʻchirib olishga, balki HD-sifatdagi seriallarni hech qanday uzilishlarsiz onlayn koʻrishga imkoniyat yaratadi.

Xizmatni yoqish: *111*2*7*1#   
Xizmatni oʻchirish: *111*2*7*2#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='voice')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🕛«Limitsiz ovoz»</b> xizmati

«Limitsiz ovoz» xizmati abonentlarga GSM va CDMA tarmoqlari ichida bepul qo‘ng‘iroqlarni amalga oshirish imkonini beradi.
Narxi 210 so‘m kuniga

Faollashtirish – *111*2*15*1#
Xizmatni o'chirish - *111*2*15*2#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='transferMB')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🛍Megabaytlarni tezkor o‘tkazish</b>

Xizmatni faollashtirish *122*99XXXXXXX * trafik# 
Misol: *122*991234567*200#  
O‘tkazmoqchi bo'lgan trafik hajmini 100, 200 yoki 300 sonlari bilan ko'rsatilishi kerak.

Bir martalik o'tkazmaning narxi 500 so'm 
O‘tkazilgan internet-trafikning amal qilish muddati - 7 kun.
Internet-trafikning maksimal hajmi kuniga: 500 MB""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='restart')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>♻️"Restart"</b>

«Restart» xizmatini muvaffaqiyatli faollashtirganda Street, Flash va Royal tariflar tizimlaridagi abonentlar oylik davrning istalgan kunida bir oylik limitlarni olishadi,
Bunda oylik abonent to‘lovining yechilish muddati yangilanadi.

Xizmatni faollashtirish *555#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='voice_mail')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🗣Ovozli pochta</b>

Ovozli pochta xizmati - bu har qanday sharoitda aloqada bo'lish imkoniyatidir! Ovozli pochta orqali siz qo'ng'iroqqa javob bera olmaganingizda, UZTELECOM abonentlari qoldirgan ovozli xabarlarni qabul qilishingiz va tinglashingiz mumkin.
Xizmat abonent to'lovini talab qilmaydi. Ovozli xabarni 6757 raqamiga qo'ng'iroq qilib bepul tinglashingiz mumkin. Shuningdek, agar xohlasangiz, avtoulov ko'rsatmalariga amal qilib o'z salomingizni yozib olishingiz mumkin. Xabar narxi - 240 so'm. Ovozli xabarning maksimal davomiyligi 60 soniya.

Xizmatni faollashtirish: *111*1*24*1#
Xizmatni o'chirish: *111*1*24*2#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='night_call')
async def lte (call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🌘Tungi qo'ng'iroqlar</b> xizmati

Xizmatni faollashtirgandan keyin, tarmoq ichida qo'ng'iroqlar, shuningdek, "O'zbektelekom" va uning filiallari liniyalarida qayd etilgan raqamlarga chiquvchi qo'ng'iroqlar (xizmat amal qilish davrida) narxlanmaydi. Xizmatni amal qilish davri: har kuni soat 22:00 dan 07:00 gacha. 
Faollashtirish narxi (bir martalik to'lov) 420 so'm. 
Abonent to'lovi kuniga 42 so'm
 
O'chirish <code>*111*1*16*2#</code>
Holatni bilish *111*1*16*3#
""", reply_markup=services)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text_contains='family')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>👨‍👨‍👦“Oila uchun”</b> xizmati

“Oila uchun” xizmati guruhi ichida cheklanmagan ovozli trafik
Narxi 210 so‘m
Amal qilish muddati kalendar oyi 

Faollashtirish *111*1*17*1*1#
Xizmatni o'chirish *111*1*17*1*2#""", reply_markup=services)

    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='hidden_call')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>⚡️«Yashirin qo‘ng‘iroq»</b>

Mazkur xizmat abonentlarga o‘z telefon raqamlarini yashirishga ruhsat beradi. Qo‘ng‘iroq qabul qilayotgan abonent, qo‘ng‘iroqni amalga oshirayotgan abonentning telefon raqamini ko‘ra olmaydi.

Xizmat Pre-paid tizimdagi abonentlarga abonent to‘lovisiz amal qiladi, hamda xizmat maxsus ulanishni talab qilmaydi.

Shartlar:

1. Mazkur xizmatdan foydalanish uchun qo‘g‘iroq amalga oshirilganda, terilayotgan raqamdan avval «#» tugmasini bosish va raqamni xalqaro formatda kiritish kerak: #99899ХХХХХХХ. Qo‘ng‘iroq yashirin holda amalga oshiriladi.
2. «Yashirin qo‘ng‘iroq» xizmati orqali qo‘ng‘iroqni amalga oshirish narxi - 210,52 so‘m.
3. «Yashirin qo‘ng‘iroq» xizmatidan foydalanilganda, «Shaxsiy raqam uzatilishini taqiqlash» xizmati yoqilgan bo‘lsa ham, xizmat uchun abonent hisobidan 210,52 so‘myechiladi.
4. Xizmatdan foydalanilganda tarif rejasi limitiga kirgan vaqt qoldig‘ini sarflamaydi. 
5. Barcha qo‘ng‘iroqlar suhbatning birinchi soniyasidan hisoblanib, daqiqa sifatida narxlanadi.
6. Xizmat faqat abonent UZMOBILE tarmog‘ida bo‘lganida amal qiladi.""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='hidden_number')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>💳Shaxsiy raqam uzatilishini taqiqlash</b>

Mazkur xizmat yashirin raqamdan qo‘ng‘iroqlar amalga oshirishga ruxsat beradi, ya’ni qo‘ng‘iroq qabul qilayotgan abonent, qo‘ng‘iroqni amalga oshirayotgan abonentning telefon raqamini ko‘ra olmaydi. 

Qo‘ng‘iroq qabul qilayotgan abonent telefonida raqam o‘rniga “Raqam yashirilgan”, “Maxfiy raqam” yoki telefon apparati turiga ko‘ra, shunga o‘xshash yozuv chiqadi. 

Xizmat abonent to‘lovi, oyiga 8400 so'm

*Xizmatni kompaniyaning ofislarida o'rnatishingiz mumkin. Hozirda USSD / SMS orqali xizmatlarni boshqarish funktsiyasini yaratish bo'yicha ishlar olib borilmoqda.""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='fast_transfer')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🔰"Tezkor o‘tkazmalar”</b> xizmati

Bu xizmat Uzmobile abonentlari oʻrtasida pul oʻtkazmalarini amalga oshirishga yordam beradi Har bir pul oʻtkazmalari miqdori butun raqamlarda koʻrsatilishi kerak 1000(1) dan 20000(20) soʻmgacha.
Mablagʻlarni UZMOBILE boshqa abonentiga oʻtkazish uchun, pul oʻtkazayotgan abonent quyidagi USSD soʻrovni amalga oshirishi kerak: Misol uchun, 99XXXABCD raqamli abonentga 3000 soʻmga teng mablagʻ yuborish uchun, yuboruvchi abonent quyidagi USSD soʻrovni yuboradi *124*3*99XXXABCD#..
Bir kunlik maksimal pul oʻtkazma miqdori 100 000 soʻmni tashkil etadi
Muvaffaqiyatli pul oʻtkazmasi uchun xizmat narxi 160 soʻm
Pul otkazilgandan keyin abonent (pul oʻtkazgan) hisobida 4000 soʻmdan kam boʻlmagan mablagʻ qolishi kerak.""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='fines')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🔖YHQ jarimalari haqida xabar</b> xizmati

GSM jismoniy va yuridik shaxslar abonentlar uchun ulanish xizmati.

YHQ buzilishi haqidagi SMS narxi – 210,52 so‘m 1 SMS
YHQ buzilishi mavjud emasligi haqidagi SMS narxi – 84,21 so‘m 1 SMS
Xizmatni boshqarish:

O‘z YHQ buzilishlari haqida xabar olish uchun quyidagi axborot bilan bepul SMS jo ‘natish zarur: 
8860 raqamiga «avtomobilning davlat raqami oрaliq bo‘sh joy qoldirish tex. pasport seriyasi va raqami» (Masalan: 01R999XY AAC5447770).
Abonent soro‘v jo‘natgan vaqtdan boshlab soro‘viga javoban nechta to‘lovi amalga oshirilmagan qoida buzilishlar bo‘lsa, shuncha sonli pulli SMS-xabar oladi.
Qoida buzish mavjud bo‘lmaganda javoban pullik quyidagi matnli SMS-xabar keladi:
«Sizda qoida buzish mavjud emas».
Agar abonent dastlabki ma’lumotlarni (avtomobilning davlat raqami oрaliq bo‘sh joy qoldirish tex. pasport seriyasi va raqami) noto‘g‘ri kiritgan bo‘lsa, javoban DYHXX raqamiga bepul SMS-xabar keladi.
Bundan tashqari, abonentlar YHQ buzilishi haqidagi axborotni dyhxx.uz portalidan olishlari mumkin. Buning uchun portalda ro‘yxatdan o‘tish, shundan keyin «Kirish» tugmasini bosish zarur, shunda sizga 8861 raqamidan «Sizning kodingiz XXXXXX» matni bilan pullik SMS jo‘natiladi.""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='load')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>☎️Chaqiriqni kutish va ushlab turish</b>
Suhbat mobaynida javob berish jarayonida boshqa abonent kirish qo'ng'iroqlari (yoki qo'ng'iroq qilgan boshqa abonent) Chaqiriqni kutish rejimi imkonini beradi va kirish chaqiriqlarini mazkur joriy suhbat tugaguniga qadar ushlab turadi, ya'ni navbatma-navbat 2 abonent bilan suhbatlashadi.
Faollashtirish kodi:  *43#
Xizmatni oʻchirish kodi: #43#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='rederect')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>⤴️Barcha qo‘ng‘iroqlarni yo‘naltirish (Shartsiz Pereadresatsiya)</b>

Faollashtirish: 21*telefon raqami#
Bekor qilish: ##21#  

Misol uchun: kiruvchi barcha qo‘ng‘iroqlarni +998991234567 raqamiga yo‘naltirish uchun, quyidagi buyruq kiritiladi: 21*+998991234567#


<b>↩️Telefon band bo‘lganda qo‘ng‘iroqlarni yo‘naltirish (Pereadresatsiya)</b>

Faollashtirish: 67*telefon raqami#
Bekor qilish:  ##67#
    
Misol uchun: telefon band bo‘lganda qo‘ng‘iroqlarni +998991234567 raqamiga yo‘naltirish uchun, quyidagi buyruq kiritiladi:  67*+998991234567#


<b>↗️Javobsiz qo‘ng‘iroqlarni yo‘naltirish (Pereadresatsiya)</b>

Faollashtirish: 61* telefon raqamiX# 
Bu yerda X = vaqt, sekundda (5 sekunddan 25 sekundgacha)

Bekor qilish: ##61#  

*Misol uchun: qo‘ng‘iroqqa 10 sekund ichida javob bo‘lmaganda, qo‘ng‘iroqlarni +998991234567 raqamiga yo‘naltirish uchun, quyidagi buyruq kiritiladi: 67*+99899123456710#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='ban')
async def lte(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>🔔Chiquvchi qo’ng’iroqlarni taqiqlash</b>

Chiquvchi qo’ng’iroqlarni taqiqlash xizmati abonentga barcha chiquvchi qo’ng’iroqlarni taqiqlash imkonini beradi.

Xizmatni yoqish: *33*0000#
Xizmatni oʻchirish: #33*0000#


<b>🔕 Kiruvchi qo’ng’iroq va SMS larni taqiqlash</b>

Kiruvchi qo’ng’iroq va SMS larni taqiqlash xizmati abonentga barcha kiruvchi qo’ng’iroq va SMSlarni taqiqlash imkonini beradi.

Xizmatni yoqish: *35*0000#
Xizmatni oʻchirish: #35*0000#""", reply_markup=services)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains='service')
async def service(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("""<b>📡Abonеnt bo‘limi xizmatlari</b>

XIZMATLAR TURI
Shartnomani qayta rasmiylashtirish* 8400 so'm
Tеlеfon raqamini almashtirish 8400 so'm
Qo‘ng‘iroqlar tafsiloti (oxirgi 3 oylik) 8400 so'm
Аbonеnt tomonidan o‘z raqamini 2 oy muddatga vaqtinchalik uzib qo‘yish bepul
Vaqtinchalik uzib qo‘yishda raqamni saqlab qo‘yish uchun to‘lov (2 oydan ortiq muddatga) 4200 so'm/oyiga
Raqamni saqlash uchun to‘lov (prepaid abonentlarga) 126 so'm/kuniga
SIM-kartalarini almashtirish 8400 so'm
Shartnomani tiklash 12500 so'm

* Pulli toifadagi raqamni qayta rasmiylashtirilganda yangi abonent pulli toifadagi raqamning 100 % narxini to‘laydi.""", reply_markup=services)
    await call.answer(cache_time=60)