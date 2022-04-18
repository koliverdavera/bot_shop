from data.database import session
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

Session = session()

default_balance = 2

REG, GIVE_PROMO, ENTER_PROMO, READY, CHANGE_REG_1, CHANGE_REG_2, ORDER, CONFIRM, FINISH = range(9)
# READY_2 - промежуточное состояние, откуда можно перейти к каталогу мерча


button = InlineKeyboardButton('Хочу мерч', callback_data='button1')
kb_start = InlineKeyboardMarkup().add(button)

button_true = InlineKeyboardButton('Оформить заказ', callback_data='confirmed_true')
button_false = InlineKeyboardButton('Назад', callback_data='confirmed_false')
kb_true_false = InlineKeyboardMarkup(row_width=1).add(button_true, button_false)

# def event_calendar_str(): result = f'📅 11 апреля (online/offline)\n\n📌 Выпускники ВШБ расскажут о карьерной
# мобильности и работе за рубежом.\n'\ 'Когда: 11 апреля в 16:00\n[Регистрация](https://vk.cc/ccxBcU)\n\n' \ '📌 Сбер
# расскажет о трендах ФинТеха на ближайшие годы: облачные решения, блокчейн, оплата по QR, перспективные российские и
# китайские решения.' \ ' Понятным языком и без лишней теории. Спикер мероприятия — Валерия Матюхина, гендиректор
# единой системы для оплаты транспорта в столице и ' \ 'регионах «СберТройка», победительница рейтинга Forbes «30 до
# 30» в категории «Управление».\nКогда: 11 апреля в 18:00\n' \ '[Регистрация](https://vk.cc/ccxE1P)\n' \ 'Мероприятие
# пройдет в гибридном формате — онлайн + офлайн в аудитории 4404. Выбирай свой вариант участия и регистрируйся!'
# result += f'\n\n\n📅 12 апреля (online)'\ '\n\n📌 Карьерное агентство Ancor: что происходит на рынке труда сегодня
# и как вести поиск работы?'\ '\nКогда: 12 апреля в 14:15'\ '\n[Регистрация](https://vk.cc/ccxKd9)'\ '\n\n📌
# Мастер-класс от Банка «Открытие»: эмоциональный интеллект и его применение в деловой коммуникации.'\ '\nКогда: 12
# апреля в 15:30'\ '\n[Регистрация](https://vk.cc/ccxKAF)'\ '\n\n📌 Компания «1С» расскажет о перспективах карьеры в
# IT-отрасли'\ '\nКогда: 12 апреля в 16:45'\ '\n[Регистрация](https://vk.cc/ccxKyd)'\ '\n\n📌 Молодёжное сообщество
# по цепям поставок: как сообщество влияет на карьеру и какие возможности для развития дает'\ '\nКогда: 12 апреля в
# 18:00'\ '\n[Регистрация](https://vk.cc/ccxKK1)' result += f'\n\n\n📅 13 апреля (offline)\n\nУчаствуй в
# офлайн-мероприятиях с 12:00 до 16:00 в коворкинге 4 корпуса. Не зацикливайся на диджитальном общении,
# особенно когда понимаешь, что оно становится слишком засоренным, выходи общаться вживую! \n' \ f'\n📌Карьерные
# консультации: как сделать «продающее резюме» и как не провалить собеседование!' \ f'\n📌Ярмарка вакансий,
# в которой примут участие в том числе:' \ f'\n - один из лидеров финтеха – Банк Тинькофф;' \ f'\n - консалтинг,
# который всегда с нами – Mazars;' \ f'\n - компания ЛУКОЙЛ, которая не нуждается в представлении, НО нуждается в
# студентах Вышки;' \ f'\n - «комбо» карьерного консультирования и экспресс-интервью от ведущего карьерного агентства
# Ancor.' \ f'\n📌16:30 От выпускников ВШБ - Молодёжного сообщества по цепям поставок - Деловая игра по эффективным
# переговорам: закупки и переговоры в управлении цепями поставок.' \ f'\n\nЦентр карьеры готов поддержать тебя в
# условиях неопределенности на рынке труда. Неизменным остаются такие качества как целеустремленность,
# кросс-функциональность и широкий бизнес-кругозор. Ситуация меняется – меняйся и ты!' \ f'\n\n📌Питч-сессия с
# Центром карьеры ВШБ' \ f'\nПитчинг – это короткое выступление перед потенциальным инвестором. А в нашем случае,
# перед гипотетическим работодателем. ' \ f'\nБудет интересно: профессиональные рекрутеры, с многолетним опытом найма
# в международные компании, - ныне сотрудники Центра карьеры, расскажут, как завоевать доверие и показать свою
# ценность с первых минут, разберут типичные ошибки и дадут важные советы. Каждый выступивший с самопрезентацией
# получит обратную связь!' \ f'\nРегистрируйся на питч-сессию, готовь самопрезентацию на 1-2 минуты!  Добавь энергии
# и эмоций, излагай свой опыт как историю!' \ f'\nКогда: 13 апреля 12:00 - 16:00 ' \ f'\n[Регистрация](
# https://docs.google.com/forms/d/1eVyH5-BN9t4HYqgddTJuxTmH2zxRpxqkYgp8GSEISJg/edit)' result += f'\n\n\n📅 14
# апреля'\ '\n\n📌 Опыт ВДНХ: как стать профессионалом в привлечении партнеров и спонсоров.' \ '\nЮлия Бояркина,
# руководитель департамента коммерческих программ и работы с партнерами, расскажет о том, ' \ 'как как стать
# профессионалом в привлечении партнеров и спонсоров, и как реализуется маркетинговая ' \ 'стратегия уникального
# комплекса ВДНХ. ' \ '\nКогда: 14 апреля в 14:15' \ '\n[Регистрация](https://vk.cc/ccxLdH)' \ '\n\n📌 PepsiCo:
# карьера в коммерческой функции FMCG компании. ' \ 'На встрече ты узнаешь о том, в какие отделы можно попасть,
# получив экономическое или бизнес-образование, ' \ 'чем интересна коммерческая функция и чем в ней заниматься,
# какие софт скиллы там востребованы, чтобы студенты ' \ 'понимали все многообразие потенциальной карьеры в FMCG
# секторе.' \ '\nКогда: 14 апреля в 15:30' \ '\n[Регистрация](https://vk.cc/ccxLms)' \ '\n\n📌 Как и куда инвестируют
# новые миллионеры? Вебинар от Тинькофф.Инвестиции.' \ '\nТы узнаешь больше про текущие тренды в инвестициях
# миллионеров,' \ 'как меняются предпочтения новых поколений состоятельных людей,' \ 'как отразился коронавирус на
# выборе инструментов инвестиций.' \ '\nКогда: 14 апреля в 19.00' \ '\n[Регистрация](https://vk.cc/ccxLK3)\n\nС
# дополнительной информацией можно ознакомиться на [сайте](https://12062014.wixsite.com/my-site-2)'
#
#     # events_db = Session.query(Event).order_by(Event.number)
#     # for event in events_db:
#     #     result += f'🔺{event.name}\n🔹{event.datetime}\n' \
#     #               f'🔹{event.description if event.description is not None else "Описание появится позже!"}\n' \
#     #               f'🔹{event.link if event.link is not None else "Ссылка появится позже!"}\n\n'
#     return result
#
#
# def companies_dict():
#     companies_db = Session.query(Company)
#     companies = dict()
#     for comp in companies_db:
#         companies[comp.name] = comp.description
#     return companies
#
#
# rules = 'Как *заработать* коины:\n2 коина — за регистрацию в чат-боте\n3 коина — за присутствие на онлайн вебинаре\n' \
#         '5 коинов — за присутствие на очном мероприятии\n' \
#         '5 коинов — за активность на вебинаре\nПо 1 коину тебе и другу — когда твой ' \
#         'друг введет промокод в чат-боте. (Твой промокод могут активировать 5 человек. ' \
#         'То есть за приглашение друзей ты можешь дополнительно получить 5 коинов)\n\nКак *потратить* коины:\n' \
#         '18 апреля я пришлю тебе сообщение, когда заказ мерча будет открыт! Ты сможешь потратить все заработанные коины на призы.' \
#         '\nПосле оформления заказа' \
#         ' приходи за честно заработанными призами в Центр карьеры (Шаболовка, корпус 4, аудитория 4401)'
#
# info = 'Неделя Карьеры ВШБ проводится на нашем факультете весной и осенью. В этот раз она пройдет с 11 по 14 апреля ' \
#        '2022 года. Мы проведем очные и онлайн мероприятия на самые разные темы.\n\nУ каждого ' \
#        'зарегистрированного в боте участника будет свой виртуальный счет с валютой ВШБ - <b>коинами</b>. Проявляя ' \
#        'активность на вебинарах, ты сможешь заработать больше коинов. По окончании Недели Карьеры ты сможешь ' \
#        'обменять их на <b>мерч</b> Высшей Школы Бизнеса (термокружки, свитшоты, блокноты, шоперы😉). \n\nС помощью бота ' \
#        'ты можешь отслеживать свой баланс, смотреть ' \
#        'актуальную' \
#        ' программу мероприятий и регистрироваться на них!\n\n'
# help_message = 'По вопросам, связанным с Неделей Карьеры, пиши на почту careers@hse.ru\n' \
#                'По вопросам работы с ботом обращайся к @koli_vera'
#
#
# welcome = "Привет! Я твой виртуальный помощник на весенней Неделе Карьеры ВШБ.\n\n" + info + 'Для начала работы ' \
#                                                                                             'нужно зарегистрироваться. ' \
#                                                                                             'Введи, пожалуйста, свои ' \
#                                                                                             'ФИО: '
# about_coins = 'После регистрации тебе доступно {} коина.'.format(default_balance)
# # help_message = 'По вопросам вопросам, связанным с Неделей Карьеры, пиши на почту careers@hse.ru\n' \
# #                'По вопросам работы с ботом обращайся к @koli_vera '
#
# keyboard_back_menu = types.InlineKeyboardMarkup()
# keyboard_back_menu.add(types.InlineKeyboardButton('В меню', callback_data='menu'))
#
# keyboard_back = types.InlineKeyboardMarkup()
# keyboard_back.add(types.InlineKeyboardButton('Назад', callback_data='menu'))
#
# keyboard_changes = types.InlineKeyboardMarkup(row_width=2)
# b1 = types.InlineKeyboardButton(text='Да', callback_data='changes_needed')
# b2 = types.InlineKeyboardButton(text='Нет', callback_data='no_changes_needed')
# keyboard_changes.add(b1, b2)
#
#
# # def get_kb_companies():
# #     keyboard_companies = types.InlineKeyboardMarkup(row_width=2)
# #     buttons = []
# #     for key, val in companies_dict().items():
# #         new_button = types.InlineKeyboardButton(text=key, callback_data=key)
# #         buttons.append(new_button)
# #     keyboard_companies.add(*buttons)
# #     keyboard_companies.add(types.InlineKeyboardButton(text='Назад', callback_data='menu'))
# #     return keyboard_companies
#
#
# # if __name__ == '__main__':
# #     keyboard_companies = get_kb_companies()
#
#
# keyboard_change_reg = types.InlineKeyboardMarkup()
# b1 = types.InlineKeyboardButton(text='Изменить ФИО', callback_data='change_fio')
# b2 = types.InlineKeyboardButton(text='Изменить email', callback_data='change_email')
# keyboard_change_reg.add(b1, b2)
#
# keyboard_promo = types.InlineKeyboardMarkup(row_width=2)
# keyboard_promo.add(types.InlineKeyboardButton(text='Да', callback_data='activate_promo'),
#                    types.InlineKeyboardButton(text='Нет', callback_data='skip_activate_promo'))
#
# keyboard_menu = types.InlineKeyboardMarkup(row_width=2)
# b1 = types.InlineKeyboardButton(text='Расписание', callback_data='event_calendar')
# b2 = types.InlineKeyboardButton(text='Правила игры', callback_data='rules')
# # b3 = types.InlineKeyboardButton(text='Работодатели', callback_data='companies')
# b4 = types.InlineKeyboardButton(text='Мой баланс', callback_data='balance')
# b5 = types.InlineKeyboardButton(text='Ввести промокод', callback_data='activate_promo')
# b6 = types.InlineKeyboardButton(text='Информация о НК', callback_data='info')
# b7 = types.InlineKeyboardButton(text='Мой профиль', callback_data='change_reg')
# keyboard_menu.add(b1, b2, b4, b5, b6, b7)
#
# keyboard_menu_light = types.InlineKeyboardMarkup(row_width=2)
# keyboard_menu_light.add(b1, b2, b4, b6, b7)
#
#
# final_intro = 'Спасибо тебе за участие в Неделе Карьеры! Ты хорошо проявил себя. Наконец-то можно обменять ' \
#               'заработанные коины на мерч ВШБ!\n'
#
# # keyboard_final = types.InlineKeyboardMarkup()
# # keyboard_final.add(types.InlineKeyboardButton(text='Оценить компании', callback_data='assess'))
#                   # types.InlineKeyboardButton(text='Каталог мерча', callback_data='catalog'))
#
#
# # def get_kb_assess():
# #     keyboard_companies = types.InlineKeyboardMarkup(row_width=2)
# #     buttons = []
# #     for key, val in companies_dict().items():
# #         new_button = types.InlineKeyboardButton(text=key, callback_data=f'{key}')
# #         buttons.append(new_button)
# #     keyboard_companies.add(*buttons)
# #     return keyboard_companies
#
#
# # kb_assess_2 = types.InlineKeyboardMarkup()
# # kb_assess_2.add(types.InlineKeyboardButton(text='Дальше', callback_data='check_assess'))
