from sqlalchemy import Column, Integer, String, BOOLEAN, ForeignKey
from data.database import Base
import itertools


class Order(Base):
    __tablename__ = 'orders'

    counter = itertools.count()
    number = Column(Integer, primary_key=True)
    fio = Column(String)
    chat_id = Column(Integer, ForeignKey('students.chat_id'))
    item_articul = Column(Integer, ForeignKey('items.articul'))
    item_amount = Column(Integer)
    confirmed = Column(BOOLEAN)

    def __init__(self, fio, chat_id, item_articul):
        self.number = next(self.counter)
        self.fio = fio
        self.chat_id = chat_id
        self.item_articul = item_articul
        self.item_amount = 1
        self.confirmed = False


