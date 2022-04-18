from variables import Session
from data.students import Student
from data.orders import Order


def get_phase(message):
    student = Session.query(Student).get(message.chat.id)
    if student is None:
        return -1
    return student.phase


def update_phase(message, new_phase):
    student = Session.query(Student).get(message.chat.id)
    student.phase = new_phase
    Session.commit()


def coins(number):
    numb = number % 100
    if numb % 10 == 1 and numb != 11:
        return 'коин'
    if (2 <= numb <= 4 or 2 <= numb % 10 <= 4) and numb not in (12, 13, 14):
        return "коина"
    else:
        return 'коинов'


def create_order(student, item_articul):
    order = Order(student.fio, student.chat_id, item_articul)
    student.order = order.number
    Session.add(order)
    Session.commit()


