import logging
from data.items import Item
from data.database import *
from aiogram import Bot, Dispatcher, executor, types
from variables import *
from functions import *

test = '2129108100:AAH_atAWSLmWPCYAhR1NopPQhJzEwk7N8Gc'
real = '5223377564:AAF_QQzyd9Y_BnkX3Vb_54R4JhmwNGKfuCQ'
chat_id_send_order = -1001763487746

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=real)
dp = Dispatcher(bot)


# @dp.callback_query_handler(lambda call: call.data == 'merch')
# async def start(call):
#     await bot.send_message(call.message.chat.id, text="Неделя Карьеры подошла к концу! Ты отлично поработал, и надеемся, получил полезный "
#                               "опыт и положительные эмоции.\n"
#                               "Наконец пришло время обменять честно заработанные коины на мерч :) ", reply_markup=kb_start)


@dp.callback_query_handler(lambda call: ENTER_PROMO < get_phase(call.message) < ORDER and call.data == 'merch')
async def merch(call):
    student = Session.query(Student).get(call.message.chat.id)
    update_phase(call.message, ORDER)
    kb_items = await Item.get_catalog(session=Session, bot=bot, chat_id=call.message.chat.id)
    if len(kb_items.inline_keyboard) == 0:
        update_phase(call.message, FINISH)
        await bot.send_message(call.message.chat.id, text=f'{student.get_balance_for_order()}\nК сожалению, '
                                                          f'на твоем счету недостаточно коинов для приобретения мерча, '
                                                          f'или весь мерч уже закончился('
                                                          f'\nЖдем тебя на следующей неделе Карьеры!')
    else:
        await bot.send_message(call.message.chat.id, f'{student.get_balance_for_order()}\nТы можешь заказать ровно '
                                                     f'один товар из каталога.', reply_markup=kb_items)


@dp.callback_query_handler(lambda call: get_phase(call.message) == ORDER)
async def enter_item(call):
    item_chosen = Session.query(Item).get(call.data)
    student = Session.query(Student).get(call.message.chat.id)
    if student.balance < item_chosen.price:
        await bot.send_message(call.message.chat.id, text='У тебя недостаточно коинов на покупку этого товара :(\nВоспользуйся кнопками из предыдущего сообщения.')
    else:
        if item_chosen.stock > 0:
            orders = Session.query(Order).filter(Order.chat_id == student.chat_id).all()
            if len(orders):
                orders[0].item_articul = item_chosen.articul
            else:
                create_order(student, item_chosen.articul)
            update_phase(call.message, CONFIRM)
            await bot.send_message(student.chat_id, f"Ты выбрал товар: {item_chosen.name}\n"
                                                    f"Подтверждаешь свой выбор?", reply_markup=kb_true_false)
        else:
            await bot.send_message(student.chat.id, "К сожалению, товар уже разобрали :(")


@dp.callback_query_handler(lambda call: call.data == 'confirmed_true' and get_phase(call.message) == CONFIRM)
async def confirm(call):
    student = Session.query(Student).get(call.message.chat.id)
    order = Session.query(Order).filter(Order.chat_id == student.chat_id).one()
    if order.confirmed:
        return
    else:
        item_chosen = Session.query(Item).get(order.item_articul)
        if item_chosen.stock > 0:
            order.confirmed = True
            student.balance -= item_chosen.price
            item_chosen.stock -= 1
            if item_chosen.stock == 0:
                await bot.send_message(chat_id_send_order, f"Товар {item_chosen.name} закончился!")
            await bot.send_message(chat_id_send_order, f"Создан новый заказ (номер {order.number})\n"
                                                       f"Студент: {student.fio}\n"
                                                       f"Почта: {student.email}\n"
                                                       f"Заказанный товар: {item_chosen.name}")
            update_phase(call.message, FINISH)
            Session.commit()
            await bot.send_message(call.message.chat.id, "Заказ успешно подтвержден. Ты можешь забрать свой мерч в Центре Карьеры"
                                                         " на Шаболовке в аудитории 4401. Спасибо за участие в Неделе Карьеры!")
        else:
            await bot.send_message(call.message.chat.id,
                                   "Мерч очень быстро разбирают, и этот товар уже закончился :(\nПожалуйста, выбери другой")
            update_phase(call.message, ORDER)
            await merch(call)


@dp.callback_query_handler(lambda call: call.data == 'confirmed_false' and get_phase(call.message) == CONFIRM)
async def change_item(call):
    update_phase(call.message, ORDER)
    await bot.send_message(call.message.chat.id, "Выбери нужный товар из доступного каталога:")
    await merch(call)


if __name__ == '__main__':
    create_db()
    try:
        Session.rollback()
        executor.start_polling(dp, skip_updates=True, timeout=None)
    except Exception as e:
        print(e)
        del bot
        bot = Bot(token=real)
        dp = Dispatcher(bot)
        