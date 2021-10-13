from config import tg_token
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
from keyboard import *
from yobit import yobit
import time
import requests
bot = Bot(token=tg_token)
dp = Dispatcher(bot)
YOBIT = yobit()
class edit():

    def set_edit_mes_id(self,edit_mes_id):
        self.edit_mes_id = edit_mes_id
    def set_edit_chat_id(self,edit_chat_id):
        self.edit_chat_id = edit_chat_id
    def get_ems(self):
        return self.edit_mes_id
    def get_eci(self):
        return self.edit_chat_id
edits=edit()
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):


    await message.answer(bold("Hello, this is bot for trading on crypto exchange")+" [YoBit](https://yobit.net/?bonus=xSdrE)",
                        parse_mode=ParseMode.MARKDOWN)
    time.sleep(1)
    inline_kb1 = InlineKeyboardMarkup(row_width=2)
    inline_btn_1 = InlineKeyboardButton('English🇬🇧', callback_data='EN')

    inline_btn_2 = InlineKeyboardButton('Русский🇷🇺', callback_data='RU')
    inline_kb1.row(inline_btn_2,inline_btn_1)
    x = await bot.send_message(message.chat.id,
        "   ||||  <i><b>Choose your language:</b></i>  ||||",
        parse_mode="HTML", reply_markup=inline_kb1)

    edits.set_edit_chat_id(message.chat.id)
    edits.set_edit_mes_id(x.message_id)



@dp.message_handler()
async  def dont_understand(message: types.Message):
    await message.answer("Sorry. I don't understand you!")

@dp.callback_query_handler(text="EN")
async def first_menu_en(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=edits.get_eci(),message_id=edits.get_ems(),text="💵<b>Test Bot</b>💸 --- To testing the bot"
                                                                                 " \n"
                                                                                 "📉<b>Rate of Coins</b>📈 --- To check current rates for coins\n"
                                                                                 "⚙️<b>Auth to YoBit</b>⚙️--- Start interacting with the bot",parse_mode="HTML",reply_markup=kb_first_menu_en)
    """
    await bot.edit_message_text(chat_id=edit_chat_id, message_id=edit_mes_id, text="<b>Do you have a YoBit account?</b>",
                                parse_mode="HTML", reply_markup=il_kb_do_u_have_acc_e)
    """
@dp.callback_query_handler(text="RU")
async def first_menu_ru(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=edits.get_eci(),message_id=edits.get_ems(),
                                text="💵<b>Тест бота</b>💸 --- Тестирование бота"
                                     "\n"
                                     "📉<b>Курс Монет</b>📈 --- Просмотр актуальных курсов монет\n"
                                     "⚙️<b>Авторизация в YoBit</b>⚙️--- Начать взаимодействие с ботом", parse_mode="HTML",
                                reply_markup=kb_first_menu_ru)
    """
    await bot.edit_message_text(chat_id=edit_chat_id, message_id=edit_mes_id, text="<b>Есть ли у вас аккаунт в YoBit?</b>",
                                parse_mode="HTML", reply_markup=il_kb_do_u_have_acc_r)
    """
@dp.callback_query_handler(text="to_rate_ru")
async def rates_ru(call: types.CallbackQuery):


    response = requests.get(
        url=f'https://yobit.net/api/3/ticker/btc_usd-btc_rur-eth_rur-eth_usd-xrp_usd-xrp_rur-doge_rur-doge_usd-lts_usd-lts_rur-trx_rur-trx_usd-doge_btc-eth_btc-dash_btc-xrp_btc-ltc_btc-ltc_rur-ltc_usd-lts_btc?ignore_invalid=1')
    print(response.text)
    last_prices = response.json()
    await bot.edit_message_text(chat_id=edits.get_eci(),message_id=edits.get_ems(),text=f"<b>📈Последний Курс на  YoBit📈</b>\n\n<i>Если монета = 0, перезагрузите</i>\n\n"
                                                                                        f"<b>BTC</b> стоит : <i>{round(last_prices['btc_usd']['last'], 2)}</i>$\t =  <i>{round(last_prices['btc_rur']['last'],2)}</i>₽\n<b>ETH</b> стоит : <i>{round(last_prices['eth_usd']['last'], 2)}</i>$\t =  <i>{round(last_prices['eth_rur']['last'],2)}</i>₽\n<b>XRP</b> стоит : <i>{round(last_prices['xrp_usd']['last'], 3)}</i>$\t =  <i>{round(last_prices['xrp_rur']['last'],3)}</i>₽\n<b>DOGE</b> стоит : <i>{round(last_prices['doge_usd']['last'], 4)}</i>$\t =  <i>{round(last_prices['doge_rur']['last'],4)}</i>₽\n"
                                                                                        f"<b>LTS</b> стоит : <i>{round(last_prices['lts_usd']['last'], 4)}</i>$\t =  <i>{round(last_prices['lts_rur']['last'],4)}</i>₽"
                                                                                        f"\n<b>LTC</b> стоит : <i>{round(last_prices['ltc_usd']['last'], 4)}</i>$\t =  <i>{round(last_prices['ltc_rur']['last'],4)}</i>₽"
                                                                                        f"\n<b>TRX</b> стоит : <i>{round(last_prices['trx_usd']['last'], 4)}</i>$\t =  <i>{round(last_prices['trx_rur']['last'],4)}</i>₽"
                                                                                        f"\n\n<b>DOGE</b> стоит : <i>{int(last_prices['doge_btc']['last'] // 0.00000001)}</i> ₿"
                                                                                        f"\n<b>ETH</b> стоит : <i>{int(last_prices['eth_btc']['last'] // 0.00000001)}</i> ₿"
                                                                                        f"\n<b>DASH</b> стоит : <i>{int(last_prices['dash_btc']['last'] // 0.00000001)}</i> ₿"
                                                                                        f"\n<b>XRP</b> стоит : <i>{int(last_prices['xrp_btc']['last'] // 0.00000001)}</i> ₿"
                                                                                        f"\n<b>LTS</b> стоит : <i>{int(last_prices['lts_btc']['last'] // 0.00000001)}</i> ₿"
                                                                                        f"\n<b>LTC</b> стоит : <i>{int(last_prices['ltc_btc']['last'] // 0.00000001)}</i> ₿"
                                ,
                                parse_mode="HTML",reply_markup=il_kb_go_back_to_menu_r)

@dp.callback_query_handler(text="to_rate_en")
async def rates_en(call: types.CallbackQuery):

    coin = 'usd'
    last_prices = requests.get(url=f'https://yobit.net/api/3/ticker/btc_usd-eth_usd-xrp_usd-doge_usd-lts_usd-trx_usd-doge_btc-eth_btc-dash_btc-xrp_btc-ltc_btc?ignore_invalid=1').json()
    await bot.edit_message_text(chat_id=edits.get_eci(),message_id=edits.get_ems(),text=f"<b>📈LAST RATES ON YoBit NOW📈</b>\n\n<i>If rate of coin = 0, refresh page</i>\n\n<b>BTC</b> costs : <i>{round(last_prices['btc_usd']['last'],2)}</i>$\n<b>ETH</b> costs : <i>{round(last_prices['eth_usd']['last'],2)}</i>$\n<b>XRP</b> costs : <i>{round(last_prices['xrp_usd']['last'],3)}</i>$\n<b>DOGE</b> costs : <i>{round(last_prices['xrp_usd']['last'],4)}</i>$\n"
                                                                                 f"<b>LTS</b> costs : <i>{round(last_prices['lts_usd']['last'],4)}</i>$"
                                                                                 f"\n<b>TRX</b> costs : <i>{round(last_prices['trx_usd']['last'],4)}</i>$"
                                                                                 f"\n\n<b>DOGE</b> costs : <i>{int(last_prices['doge_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>ETH</b> costs : <i>{int(last_prices['eth_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>DASH</b> costs : <i>{int(last_prices['dash_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>XRP</b> costs : <i>{int(last_prices['xrp_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>LTC</b> costs : <i>{int(last_prices['ltc_btc']['last']//0.00000001)}</i> ₿",
                                parse_mode="HTML",reply_markup=il_kb_go_back_to_menu_e)
@dp.callback_query_handler(text="to_rate_en")
async def rates_en(call: types.CallbackQuery):


    last_prices = requests.get(url=f'https://yobit.net/api/3/ticker/btc_usd-eth_usd-xrp_usd-doge_usd-lts_usd-trx_usd-doge_btc-eth_btc-dash_btc-xrp_btc-ltc_btc?ignore_invalid=1').json()
    await bot.edit_message_text(chat_id=edits.get_eci(),message_id=edits.get_ems(),text=f"<b>📈LAST RATES ON YoBit NOW📈</b>\n\n<i>If rate of coin = 0, refresh page</i>\n\n<b>BTC</b> costs : <i>{round(last_prices['btc_usd']['last'],2)}</i>$\n<b>ETH</b> costs : <i>{round(last_prices['eth_usd']['last'],2)}</i>$\n<b>XRP</b> costs : <i>{round(last_prices['xrp_usd']['last'],3)}</i>$\n<b>DOGE</b> costs : <i>{round(last_prices['xrp_usd']['last'],4)}</i>$\n"
                                                                                 f"<b>LTS</b> costs : <i>{round(last_prices['lts_usd']['last'],4)}</i>$"
                                                                                 f"\n<b>TRX</b> costs : <i>{round(last_prices['trx_usd']['last'],4)}</i>$"
                                                                                 f"\n\n<b>DOGE</b> costs : <i>{int(last_prices['doge_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>ETH</b> costs : <i>{int(last_prices['eth_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>DASH</b> costs : <i>{int(last_prices['dash_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>XRP</b> costs : <i>{int(last_prices['xrp_btc']['last']//0.00000001)}</i> ₿"
                                                                                 f"\n<b>LTC</b> costs : <i>{int(last_prices['ltc_btc']['last']//0.00000001)}</i> ₿",
                                parse_mode="HTML",reply_markup=il_kb_go_back_to_menu_e)





if __name__ == "__main__":
    executor.start_polling(dp)

