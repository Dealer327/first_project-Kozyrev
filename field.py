"""Модуль реализации функции о сделанных ходах в текущей партии"""

# ИСПРАВИТЬ: что значит функция хранения? может, преобразования?
def turnsgame():
    """Функция хранения ходов в текущей партии"""
    # ОТВЕТИТЬ: что здесь для чего служит? откуда функция получает данные? нет ни глобальных переменных, ни параметров функции - локальные какие-то литеральные значения непонятно откуда и непонятно куда
    turns = [' ' for _ in range(9)]
    player_pos = {'X': [], 'O': []}
    return turns

turns = turnsgame()


def show_field(turns):
    """Функция отрисовки игрового поля"""
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(turns[0], turns[1], turns[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(turns[3], turns[4], turns[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(turns[6], turns[7], turns[8]))
    print("\t     |     |")
    print("\n")

show_field(turns)