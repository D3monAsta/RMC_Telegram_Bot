from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

mainCommandButton1 = KeyboardButton('Задать вопрос')
mainCommandButton2 = KeyboardButton('Поделиться информацией')

askButton1 = KeyboardButton('Да')
askButton2 = KeyboardButton('Нет')

inlineInfAboutButton = InlineKeyboardButton('О нас', callback_data='SendAboutInfo', url='https://rmc61.ru/company/')
inlineCertificateButton = InlineKeyboardButton('Как получить сертификат', callback_data='SendCertificate', url='https://rmc61.ru/services/sotsialnyy-sertifikat-dopolnitelnogo-obrazovaniya/')
inlineMocButton = InlineKeyboardButton('МОЦ', callback_data='SendOurChannels', url='https://www.rmc61.ru/contacts/')
inlineInfInfoButton = InlineKeyboardButton('Полезная информация', callback_data='SendInfo', url='https://rmc61.ru/services/')
inlineContactsButton = InlineKeyboardButton('Контакты', callback_data='SendUsNews', url='https://rmc61.ru/company/requisites/')

inlineRMCVK = InlineKeyboardButton('РМЦ в ВК', url='https://m.vk.com/rmcro')
inlineRMCOK = InlineKeyboardButton('РМЦ в ОК', url='https://ok.ru/rmcro')

inf_kb = InlineKeyboardMarkup(row_width=2).add(inlineInfAboutButton, inlineCertificateButton)
inf_kb.row(inlineMocButton)
inf_kb.add(inlineInfInfoButton)
inf_kb.add(inlineContactsButton)

# infoRequest_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Send contact ☎️', request_contact=True)).add(KeyboardButton('Send geo 🗺️', request_location=True))
main_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(mainCommandButton1).add(mainCommandButton2)
ask_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(askButton1).add(askButton2)
rmc_kb = InlineKeyboardMarkup(row_width=2).add(inlineRMCVK, inlineRMCOK)