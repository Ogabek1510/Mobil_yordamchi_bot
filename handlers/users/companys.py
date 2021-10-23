from aiogram.types import Message
from keyboards.inline.menuUzmob import uzmob
from keyboards.inline.menuMobiuz import mobiuz
from keyboards.inline.menuBeeline import beeline
from keyboards.inline.menuUcell import ucell
from loader import dp

@dp.message_handler(text_contains=('Uzmobile'))
async def select_category(message: Message):
    await message.answer("<b>🔵 Uzmobile aloq operatorining tarif, xizmat, paket va USSD kodlari:</b>", reply_markup=uzmob)

@dp.message_handler(text_contains=('Mobiuz'))
async def select_category(message: Message):
    await message.answer("<b>🔴 Mobiuz aloqa operatorining tarif, xizmat, paket va USSD kodlari:</b>", reply_markup=mobiuz)

@dp.message_handler(text_contains=('Beeline'))
async def select_category(message: Message):
    await message.answer("<b>🐝 Beeline aloqa operatorining tarif, xizmat, paket va USSD kodlari:</b>", reply_markup=beeline)

@dp.message_handler(text_contains=('Ucell'))
async def select_category(message: Message):
    await message.answer("<b>🟣 Ucell aloqa operatorining tarif, xizmat, paket va USSD kodlari:</b>", reply_markup=ucell)