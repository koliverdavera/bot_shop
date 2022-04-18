from sqlalchemy import Column, Integer, String, ForeignKey
from data.database import Base
from data.students import Student
import time
from functions import update_phase
from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


class Item(Base):
    __tablename__ = "items"

    articul = Column(Integer, primary_key=True)
    price = Column(Integer)
    stock = Column(Integer)
    photo_file_name = Column(String)
    name = Column(String)

    def __repr__(self):
        return f'{self.name}\nДоступное количество: {self.stock}\nЦена: {self.price} {self.get_price()}'

    @classmethod
    async def get_catalog(cls, session, bot, chat_id):
        student = session.query(Student).get(chat_id)
        balance = student.balance
        items = session.query(Item).filter(Item.stock >= 1)
        kb_items = InlineKeyboardMarkup()
        if len(list(items)):
            await bot.send_message(chat_id, "Вот каталог доступного мерча:")
            for item in items:
                photo = open(f'./photos/{item.photo_file_name}', 'rb')
                await bot.send_photo(chat_id, photo=photo, caption=item)
                time.sleep(1.5)
                button = InlineKeyboardButton(item.name, callback_data=item.articul)
                if item.price <= balance:
                    kb_items.add(button)
            return kb_items
        else:
            await bot.send_message(chat_id, text='К сожалению, весь мерч уже разобрали(\nЖдем тебя на следующих '
                                                 'мероприятиях Центра Карьеры!')


    def get_price(self):
        numb = self.price % 100
        if numb % 10 == 1 and numb != 11:
            return 'коин'
        if (2 <= numb <= 4 or 2 <= numb % 10 <= 4) and numb not in (12, 13, 14):
            return "коина"
        else:
            return 'коинов'
