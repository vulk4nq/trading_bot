from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
dictionary = {
    1: {
        "ru": "Русский🇷🇺",
        "en": "English🇬🇧"
    }

}
kb_first_menu_en = InlineKeyboardMarkup()
btn_to_test_e = InlineKeyboardButton('💵Test Bot💸',callback_data='to_test_en')
btn_to_check_rate_e = InlineKeyboardButton('📉Rate of Coins📈',callback_data='to_rate_en')
btn_to_auth_e = InlineKeyboardButton('⚙️Auth to YoBit⚙️', callback_data='to_auth_en')
kb_first_menu_en.add(btn_to_auth_e)
kb_first_menu_en.row( btn_to_test_e, btn_to_check_rate_e)

kb_first_menu_ru = InlineKeyboardMarkup()
btn_to_test_r = InlineKeyboardButton('💵Тест Бота💸',callback_data='to_test_ru')
btn_to_check_rate_r = InlineKeyboardButton('📉Курс Монет📈',callback_data='to_rate_ru')
btn_to_auth_r = InlineKeyboardButton('⚙️Авторизация в YoBit⚙️', callback_data='to_auth_ru')
kb_first_menu_ru.add(btn_to_auth_r)
kb_first_menu_ru.row(btn_to_test_r, btn_to_check_rate_r)


il_kb_do_u_have_acc_e = InlineKeyboardMarkup()
inline_btn_YES_e = InlineKeyboardButton('Yes✅', callback_data='Yes-i-have-account_e')
inline_btn_NO_e = InlineKeyboardButton('No❌', callback_data='No-i-havent-account_e')
il_kb_do_u_have_acc_e.row(inline_btn_YES_e,inline_btn_NO_e)

il_kb_do_u_have_acc_r = InlineKeyboardMarkup()
inline_btn_YES_r = InlineKeyboardButton('Да✅', callback_data='Yes-i-have-account_r')
inline_btn_NO_r = InlineKeyboardButton('Нет❌', callback_data='No-i-havent-account_r')
il_kb_do_u_have_acc_r.row(inline_btn_YES_r,inline_btn_NO_r)

il_kb_go_back_to_menu_e = InlineKeyboardMarkup()
inline_btn_go_back_e = InlineKeyboardButton('⏪Go Back⏪',callback_data='EN')
il_kb_go_back_to_menu_e.add(inline_btn_go_back_e)

il_kb_go_back_to_menu_r = InlineKeyboardMarkup()
inline_btn_go_back_r = InlineKeyboardButton('⏪Вернуться в меню⏪',callback_data='RU')
il_kb_go_back_to_menu_r.add(inline_btn_go_back_r)

